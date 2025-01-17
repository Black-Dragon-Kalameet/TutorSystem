from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import User
from django import forms
from . import models


class adminlog(forms.ModelForm):
     class Meta:
          model= models.admin
          fields = ('name','password')


class sloginform(forms.ModelForm):
     class Meta:
          model= models.student
          fields = ('username','password')



class tutorloginform(forms.ModelForm):
     class Meta:
          model= models.tutor
          fields = ('username','password')

class messageform(forms.ModelForm):
    class Meta:
        model = models.message
        fields = ['message', 'attachment']
        receiver = forms.ChoiceField() 

class addstudent(forms.ModelForm):
     class Meta:
          model= models.student
          fields = ['Student_name', 'username', 'email', 'phone_number', 'date_of_birth', 'profile_picture','password']

class addtutor(forms.ModelForm):
     class Meta:
          model= models.tutor
          fields = ['tutorname', 'username', 'email', 'phone_number', 'date_of_birth', 'profile_picture','password','subject']
     
class supdateprofile(forms.ModelForm):
     class Meta:
          model= models.student
          fields = ('email','phone_number','profile_picture','password')

class tutorupdateprofile(forms.ModelForm):
     class Meta:
          model= models.tutor
          fields = ('email','phone_number','profile_picture','password')

class faqform(forms.ModelForm):
    class Meta:
        model = models.faq
        fields = ['question','answer']


class testform(forms.ModelForm):
     class Meta:
          model = models.test
          fields = ['testname']

class qform(forms.ModelForm):
     class Meta: 
          model = models.quesntione
          fields = ['quesntionw']

class ansform(forms.ModelForm):
     class Meta: 
          model = models.quesntione
          fields = ['answerw']


class addbook(forms.ModelForm):
    class Meta:
        model = models.library
        fields = ['file', 'title', 'description']