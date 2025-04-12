import datetime
from django.http import HttpResponse
from django.shortcuts import render 

def home(request):
    isActive =True
    if request.method == "POST":
        check=request.POST.get("check")
        print(check)
        if check is None:isActive=False
        else:isActive=True
        name=request.POST.get("name")
        print(name)

    date= datetime.datetime.now() 

    name="Gajendra kumar Dave"

    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers form 1 to 100',
        'WAP to print pascals triangle'
    ]

    student={
        'student_name':'Rahul',
        'student_college':'xyz',
        'student_city':'Udaipur'
    }

    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student,
    }

    return render(request,'index.html',data)

def about(request):
    return render(request,"about.html",{})

def services(request):
    return render(request,"services.html",{})