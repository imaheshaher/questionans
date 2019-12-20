from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import *
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.utils import timezone
from django.contrib.postgres.search import SearchVector
# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

def register(request):

    if request.method == 'POST':
        form = userForm(request.POST)
         
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password)
            user.save()
            return HttpResponseRedirect('login')
    else:
        form = userForm()
    return render(request,'register.html',{'form':form})

def userlogin(request):
    if request.method == 'POST':
        form = userLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username = username,password = password)

            if user is not None:
                login(request,user)
                user = User()
                return HttpResponseRedirect('questionpost',{'user' : user})
            else:
                return HttpResponseRedirect('login')

    else:
        form = userLogin()
    return render(request,'login.html',{'form' : form})

def questionpost(request):
    if request.method == 'POST':
        form = Questionpost(request.POST)
        form1 = Answer(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('disp_question')
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect('disp_question')
        else:
            return HttpResponseRedirect('welcome')
        
    else:
        form = Questionpost()
        form1 = Answerpost()
    return render(request,'question.html',{'form' : form, 'form1' : form1})

def disp_question(request):
    question = Question.objects.order_by('-pub_date')
    return render(request,'disp_question.html',{'question': question})

def search_question(request):
    if request.method == 'POST':
        que = request.POST['quesearch']
        s1 = Question.objects.filter(Q(question_text__icontains = que))
        return render(request,'search_question.html',{'s1' : s1})

    return render(request,'search.html')
def onlyquestion(request):
    if request.method=='POST':
        form = quechoice(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("disp_question")
    else:
        form = quechoice()
    return render(request,'onlyquestion.html',{'form' : form})

def choice(request):
    ch = Choice.objects.all()
    return render(request,'disp_choice.html',{'ch' : ch})

def answer(request):
    if request.method == "POST":
        ans = request.method['ans']
        a = Question.objects.Create(answer_text = ans)
        a.save()
    q = Question.objects.order_by('-pub_date')
    return render(request,'answer.html',{'q' :q})