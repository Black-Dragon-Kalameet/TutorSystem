from django.shortcuts import render,redirect
from django.contrib.auth import logout

from . import models
from . import forms

# Create your views here.
def home(request):

    return render(request, 'home.html')



def tutorlogin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        X = models.tutor.objects.filter(username=username, password=password).count()
        if X > 0:
                    tutor = models.tutor.objects.filter(username=username, password=password).first()
                    request.session['tutorlogin'] = True
                    request.session['tutorid'] = tutor.id
                    print("User authenticated:", request.user.is_authenticated)
                    print("Student login session:", request.session.get('tutorlogin'))
                    return redirect('tutor/tutorview')
        else:
         return redirect('tutor/tutorlogin')
    form = forms.tutorloginform
    return render(request,'tutor/tutorlogin.html',{'form':form})






def slogin(request):
    message = ''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            student = models.student.objects.get(username=username,password=password)
            request.session['slogin'] = True
            request.session['studentid'] = student.id
            print("User authenticated:", request.user.is_authenticated)
            print("Student login session:", request.session.get('slogin'))
            return redirect('student/studentdash')


        except models.student.DoesNotExist:
            message ='wrong'

    form = forms.sloginform
    return render(request,'student/slogin.html',{'form':form, 'message': message})






