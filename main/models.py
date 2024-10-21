from django.db import models
from django.utils.html import mark_safe 

class tutor(models.Model):
    tutorname = models.CharField(max_length=180)
    username = models.CharField(null=True)
    password=models.CharField(null=True)
    subjects = [('Mat','Math'),('Sci','Science'),('Eng','English')]
    subject = models.CharField(max_length=3,choices=subjects,default='Eng')

    def __str__(self):
        return self.tutorname
    


class student(models.Model):
    Student_name = models.CharField(max_length=180, null=True)
    username = models.CharField(max_length=180, null=True)
    password = models.CharField(max_length=180,null=True)

class carosel(models.Model):
    img=models.ImageField(upload_to="carosel/")
    alt_text=models.CharField(max_length=150)

    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>' % (self.img.url))
