from django.db import models
from django.utils.html import mark_safe 

class tutor(models.Model):
    tutorname = models.CharField
    username = models.CharField(null=True)
    password=models.CharField(null=True)
    subjects = [('Mat','Math'),('Sci','Science'),('Eng','English')]
    subject = models.CharField(max_length=3,choices=subjects,default='Eng')


class student(models.Model):
    Student_name = models.CharField(max_length=180, null=True)
    username = models.CharField(max_length=180, null=True)
    password = models.CharField(max_length=180,null=True)

