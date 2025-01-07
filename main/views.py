from django.shortcuts import render,redirect,get_object_or_404
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

    return render(request, 'message.html', {'allmessages': allmessages,'form': form,'recipient': recipient,})


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


def showfaq(request):

    faqs =  models.faq.objects.all()

    return render(request, 'showfaq.html', {'faqs':faqs})


def addfaq(request):
    if request.method == 'POST':
        form = forms.faqform(request.POST)
        if form.is_valid():
            faqq = form.save(commit=False)
            tutorid =  models.tutor.objects.get(id=request.session['tutorid'])
            if not tutorid:
                return redirect('home')
            faqq.creator = tutorid 
            faqq.save()
            return redirect('showfaq')  
    else:
        form = forms.faqform()

    faqs = models.faq.objects.all()
    return render(request, 'addfaq.html', {'form': form, 'faqs': faqs})



def editfaq(request, id):
    faqq = models.faq.objects.get(id=id)
    if request.method == 'POST':
        form = forms.faqform(request.POST, instance=faqq)
        if form.is_valid():
            form.save()
            return redirect('addfaq')  
    else:
        form = forms.faqform(instance=faqq)

    faqs = models.faq.objects.all()
    return render(request, 'addfaq.html', {'form': form, 'faqs': faqs})




def deletefaq(request, id):
    faqq = models.faq.objects.get(id=id)
    faqq.delete()
    return redirect('showfaq')



def addtest(request):
    alltests = models.test.objects.all() 

    if request.method == 'POST':
        form = forms.testform(request.POST) 
        if form.is_valid():

            new_test = form.save(commit=False)
            new_test.save()  


            return redirect('addtests')  
    else:
        form = forms.testform()  

    return render(request, 'tests/addtests.html', {'form': form, 'alltests':alltests})


def deletetest(request, id):
    test = models.test.objects.get(id=id)
    test.delete()
    return redirect('tests/addtests.html')

def addquestion(request, test_id):
    
    test = models.test.objects.get(id=test_id)
    questions = test.questions.all()
    if request.method == 'POST':
        form = forms.qform(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.test = test  
            question.save()
            return redirect('addquestion', test_id=test.id)  
    else:
        form = forms.qform()

    return render(request, 'tests/addquestion.html', {'form': form, 'test': test, 'questions': questions})

def deletequestion(request, id,test_id):
    test = models.test.objects.get(id=test_id)
    question = models.quesntione.objects.get(id=id)
    question.delete()
    return redirect('addquestion', test_id=test.id)


def editquestion(request, id, test_id):
    test = models.test.objects.get(id=test_id)
    question = models.quesntione.objects.get(id=id)

    if request.method == 'POST':
        form = forms.qform(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('addquestion', test_id=test.id)  
    else:
        form = forms.qform(instance=question)

    questions = models.quesntione.objects.filter(test=test)

    return render(request, 'tests/addquestion.html', {'form': form,'questions': questions,'test': test})


def selecttest(request):
    tests = models.test.objects.all()

    return render(request, 'tests/selecttest.html', {'tests': tests})

def viewtest(request, test_id):
    test = models.test.objects.get(id=test_id)
    
    questions = test.questions.all()

    return render(request, 'tests/viewtest.html', {'test': test, 'questions': questions})


def answertest(request, test_id):
    
    test = models.test.objects.get(id=test_id)
    questions = test.questions.all()

    if 'slogin' in request.session and request.session['slogin'] == True:
        examerid = request.session.get('studentid')
        
        examinee = models.student.objects.get(id=examerid)

        if not test.examinee:
            test.examinee = examinee
            test.save()

    if request.method == 'POST':
        for question in questions:
            answer_key = f'answer_{question.id}'
            answer = request.POST.get(answer_key)
            if answer:
                question.answerw = answer  
                question.save()

        test.completed = True    
        test.timestamp = timezone.now()
        test.save()
        return redirect('viewtest', test_id=test.id)
    return render(request, 'tests/answertest.html', {'test': test, 'questions': questions})


def selecttest2(request):
    tests = models.test.objects.all()

    return render(request, 'tests/selecttest2.html', {'tests': tests})


def sendann(request):
    students = models.student.objects.all()
    tutor = request.session['tutorid']
    
    if request.method == 'POST':
        for student in students:
            form = forms.messageform(request.POST)
            
            if form.is_valid():
                message = form.save(commit=False)
                message.receiver_student = student  
                message.sender_tutor = models.tutor.objects.get(id=tutor)  
                message.save()
                
    form = forms.messageform()  
    return render(request, 'sendann.html', {'form': form})
