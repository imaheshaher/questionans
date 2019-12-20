from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm,Loginform,studentinfo
from django.db.models import *
from .models import Student
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def welcome(request):
    return render(request,"welcome.html")


def studentreg(request):

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            form.save()
            User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password)
            return render(request,'welcome.html')
    else:
        form = StudentForm()
    return render(request,"studentreg.html",{'form' : form})



    def studentlogin(request):
        if request.method == "POST":
            form = Loginform(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = auth.authenticate(request,username=username,password=password)
                return render(request,'welcome.html')
        else:
            form = Loginform()
        return render(request,'login.html',{'form' :form})

def studinfo(request):
    if request.method == 'POST':
            name = request.POST['name']
            info = Student.objects.filter(first_name__icontains=name)
            return render(request,'student_info.html',{'form' : info})
    return render (request,'student_search.html')