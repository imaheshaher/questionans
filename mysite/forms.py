from .models import Student
from django import forms
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = Student
        fields = ['first_name','last_name','username','password']


class Loginform(forms.Form):

    username  = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())


class studentinfo(forms.Form):
     name = forms.CharField(max_length=30)

