from django.urls import path
from .import views


urlpatterns = [

    path('',views.welcome,name='welcome'),
    path('student',views.studentreg,name='studentreg'),
    path('student/search',views.studinfo,name='studentinfo')
   # path('login',views.studentlogin,name='login')
]