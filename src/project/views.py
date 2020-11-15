from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import login,authenticate
from .forms import *
def home(request):
    if request.method =='POST':
       form=UserCreationForm(request.POST) 
       username=''
       password=''
       if form.is_valid():
            username=request.POST['username']
            password=request.POST['password1']
            form.save()
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/posts/')          
    else:
        form=UserCreationForm()
            
    context={
        'form':form
    }
    
    return render(request,'main/home.html',context)


