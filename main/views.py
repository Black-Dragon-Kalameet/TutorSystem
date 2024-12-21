from django.shortcuts import render,redirect
from django.contrib.auth import logout

from . import models
from . import forms
from django.utils import timezone

# Create your views here.
def home(request):
     carosels = models.carosel.objects.all()

     return render(request, 'home.html',{'carosels':carosels})



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
                    return redirect('message')
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
            return redirect('message')


        except models.student.DoesNotExist:
            message ='wrong'

    form = forms.sloginform
    return render(request,'student/slogin.html',{'form':form, 'message': message})

def studentprof(request):
    msg =None
    sid =  request.session['studentid']
    student = models.student.objects.get(id=sid)
    if request.method == 'POST':
       form = forms.supdateprofile(request.POST,request.FILES,instance=student)
       if form.is_valid:
           form.save()
           msg ='profile updated'
    
    form = forms.supdateprofile(instance=student)
    return render(request,'student/studentprof.html',{'form':form,'msg':msg})

def logouta(request):
    if 'tutorlogin' in request.session:
        del request.session['tutorlogin']
    if 'tutorid' in request.session:
        del request.session['tutorid']

    if 'slogin' in request.session:
        del request.session['slogin']
    if 'studentid' in request.session:
        del request.session['studentid']


    return redirect('home')  



def message(request, recipient_id=None):
    if recipient_id is None:
        return redirect('select_recipient')  

    form = forms.messageform()
    allmessages = []

    if 'tutorlogin' in request.session and request.session['tutorlogin'] == True:
        sender_id = request.session['tutorid']
        recipient = models.student.objects.get(id=recipient_id)
        allmessages = models.message.objects.filter(
            sender_tutor=sender_id, receiver_student=recipient_id
        ) | models.message.objects.filter(
            sender_student=recipient_id, receiver_tutor=sender_id
        )
    else:
        sender_id = request.session['studentid']
        recipient = models.tutor.objects.get(id=recipient_id)
        allmessages = models.message.objects.filter(
            sender_student=sender_id, receiver_tutor=recipient_id
        ) | models.message.objects.filter(
            sender_tutor=recipient_id, receiver_student=sender_id
        )

    if request.method == 'POST':
        form = forms.messageform(request.POST, request.FILES)
        if form.is_valid():
            message_instance = form.save(commit=False)
            if 'tutorlogin' in request.session and request.session['tutorlogin'] == True:
                message_instance.sender_tutor = models.tutor.objects.get(id=sender_id)
                message_instance.receiver_student = models.student.objects.get(id=recipient_id)
            else:
                message_instance.sender_student = models.student.objects.get(id=sender_id)
                message_instance.receiver_tutor = models.tutor.objects.get(id=recipient_id)
            message_instance.save()
            return redirect('message', recipient_id=recipient_id)

    return render(request, 'message.html', {
        'allmessages': allmessages,
        'form': form,
        'recipient': recipient,
    })


def select_recipient(request):
    available_recipients = []

    if 'tutorlogin' in request.session and request.session['tutorlogin'] == True:

        available_recipients = models.student.objects.all()
    else:
        available_recipients = models.tutor.objects.all()

    return render(request, 'select_recipient.html', {'available_recipients': available_recipients})


def library(request):
    documents = models.library.objects.all()
    return render(request, 'library.html', {'documents': documents})



def contactus(request):
    return render(request, 'contactus.html')