from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp ,Testimonial,Feedback
from .forms import EmpForm,FeedbackForm
# Create your views here

def employee(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{'emps':emps})