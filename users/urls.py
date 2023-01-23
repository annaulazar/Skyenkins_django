from django.urls import path

from users.apps import UsersConfig
from users.views import UserLogin, UserRegister

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    # path('register/', UserRegister.as_view(), name='register'),

]