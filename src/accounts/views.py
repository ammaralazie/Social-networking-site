from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate ,login,logout
# Create your views here.


def logout_view(request):
    logout(request)
    print('logout is success')
    return redirect('home')


