from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_lk, name='lk'),
    # path('login', views.users_login, name='login'),
    # path('register', views.users_register, name='register'),
]