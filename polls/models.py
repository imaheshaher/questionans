from django.db import models
import datetime
from django.utils import timezone
# Create your models here.



class Userform(models.Model):

    first_name = models.CharField(max_length=30)
    lasst_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    answer_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

