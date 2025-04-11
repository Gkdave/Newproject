from django.shortcuts import render

# Create your views here.

def user_register(request):
    if request.method=="POST":
        fname=request.POST.get['firstname']
        lname=request.POST.get['lastname']
        uname=request.POST.get['username']