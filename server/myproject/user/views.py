from django.shortcuts import render,redirect 
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.forms import PasswordChangeForm 
# Create your views here.

def user_register(request):
    if request.method=="POST":
        fname=request.POST.get['firstname']
        lname=request.POST.get['lastname']
        uname=request.POST.get['username']
        email=request.POST.get['email']
        pass1=request.POST.get['password1']
        pass2=request.POST.get['password2']
        if pass1 !=pass2 :
            messages.warning(request,"password does not match")
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'email already taken')
            return redirect('register')
        else:
            user=User.objects.create_user(first_name=fname,last_name=lname,email=email,password=pass1)
            user.save()
            messages.success(request,"user has been register successfully")
            return redirect('login')
    return render(request,'user/register.html')

def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            message.warning(request,"Invalid Credentials")
            return redirect('login')
    return render(request,'user/login.html')
    
def user_logout(request):
    logout(request)
    return redirect('login') 

def change_password(request):
    pass 