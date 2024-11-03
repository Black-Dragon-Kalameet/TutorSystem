from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import User
from django import forms
from . import models


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

     

