from django.db import models
from django.utils.html import mark_safe 
from django.utils import timezone


class tutor(models.Model):
    tutorname = models.CharField(max_length=180)
    username = models.CharField(null=False)
    password=models.CharField(null=False)
    subjects = [('Mat','Math'),('Sci','Science'),('Eng','English')]
    
    subject = models.CharField(max_length=3,choices=subjects,default='Eng')

    def __str__(self):
        return self.tutorname
    


class student(models.Model):
    Student_name = models.CharField(max_length=180, null=False)
    username = models.CharField(max_length=180, null=False)
    password = models.CharField(max_length=180,null=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    def __str__(self):
     return self.Student_name

class carosel(models.Model):
    img=models.ImageField(upload_to="carosel/")
    alt_text=models.CharField(max_length=150)

    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>' % (self.img.url))

class message(models.Model):
    sender_tutor = models.ForeignKey(tutor, on_delete=models.CASCADE, null=True, blank=True)
    sender_student = models.ForeignKey(student, on_delete=models.CASCADE, null=True, blank=True)
    receiver_tutor = models.ForeignKey(tutor, on_delete=models.CASCADE, related_name="received_messages_tutor", null=True, blank=True)
    receiver_student = models.ForeignKey(student, on_delete=models.CASCADE, related_name="received_messages_student", null=True, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return f"Message from {self.sender_tutor or self.sender_student} to {self.receiver_tutor or self.receiver_student}"


class library(models.Model):
    file = models.FileField(upload_to='library/')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    creator = models.ForeignKey(tutor,on_delete=models.CASCADE)

    def __str__(self):
     return self.question



class test(models.Model):
    testname = models.CharField(max_length=200) 
    examinee = models.ForeignKey(student, on_delete=models.SET_NULL, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
     return self.testname
    
class quesntione(models.Model):
   quesntionw = models.CharField(max_length=200)
   answerw = models.CharField(max_length=200)
   test = models.ForeignKey(test, related_name='questions', on_delete=models.CASCADE)

   def __str__(self):
     return self.quesntionw