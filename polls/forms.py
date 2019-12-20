from django import forms
from .models import Userform,Question,Choice,Answer
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class userForm(forms.Form):
    first_name = forms.CharField(widget = forms.TextInput ( attrs={'placehoder':'Enter First Name'}))
    last_name = forms.CharField(widget = forms.TextInput ( attrs={'placehoder':'Enter Last Name'}))
    username = forms.CharField(widget = forms.TextInput ( attrs={'placehoder':'Enter username'}))
    password = forms.CharField(widget = forms.PasswordInput ( attrs={'placehoder':'Enter password'}))


class Meta:
    model = userForm
    fields = ['first_name','last_name','username','password']


class userLogin(forms.Form):
    username = forms.CharField(widget = forms.TextInput (attrs={'placeholder' : 'username'}))
    password = forms.CharField(widget = forms.PasswordInput (attrs={'placeholder' : 'password'}))


class Login:
    model = userLogin

    fields = ['username','password']



class Questionpost(forms.ModelForm):


    class Meta:
        model = Question
        fields = ['question_text','answer_text']

class quechoice(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ['question','choice_text','votes']
        
class Answerpost(forms.ModelForm):

    class Meta:
        model = Answer 
        fields = ['question','answer_text']
