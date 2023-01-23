from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from users.forms import UserLoginForm

class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'



class UserRegister():
    pass
