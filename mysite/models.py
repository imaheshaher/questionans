from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):

    first_name=models.CharField(max_length=30)

    last_name=models.CharField(max_length=30)

    username=models.CharField(max_length=30)

    password=models.CharField(max_length=30)


    def __str__(self):
        return self.first_name

