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


def message(request):
    form = forms.messageform()  
    allmessages = []
    available_receivers = []  


    if 'tutorlogin' in request.session and request.session['tutorlogin'] == True:
        id = request.session['tutorid']
        allmessages = models.message.objects.filter(sender_tutor=id) | models.message.objects.filter(receiver_tutor=id)
        available_receivers = models.student.objects.all() 
    else:
        id= request.session['studentid']
        allmessages = models.message.objects.filter(sender_student=id) | models.message.objects.filter(receiver_student=id)
        available_receivers = models.tutor.objects.all()  

    if request.method == 'POST':
        form = forms.messageform(request.POST, request.FILES)
        if form.is_valid():
            message_instance = form.save(commit=False)
            receiver_id = request.POST.get('receiver_id')  
            if request.session['tutorlogin'] == True:
                id2= request.session['tutorid']
                message_instance.sender_tutor = models.tutor.objects.get(id=id2)
                message_instance.receiver_student = models.student.objects.get(id=receiver_id)
            else:
                id2= request.session['studentid']
                message_instance.sender_student = models.student.objects.get(id=id2)
                message_instance.receiver_tutor = models.tutor.objects.get(id=receiver_id)

            message_instance.save()
            return redirect('message')

    return render(request, 'message.html', {
        'allmessages': allmessages,
        'form': form,
        'available_receivers': available_receivers,  
    })


