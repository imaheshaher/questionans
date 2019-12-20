from django.urls import path


from . import views

urlpatterns = [
        path('welcome',views.welcome,name='welcome'),
        path('register',views.register,name='register'),
        path('login',views.userlogin,name = 'login'),
        path('questionpost',views.questionpost,name='questionpost'),
        path('disp_question',views.disp_question,name='disp_question'),
        path('search_question',views.search_question,name='search_question'),
        path('onlyquestion',views.onlyquestion,name = 'onlyquestion'),
        path('answer',views.answer,name='answer'),
        path('choice',views.choice,name='choice')
]