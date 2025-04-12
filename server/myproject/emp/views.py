from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp ,Testimonial,Feedback
from .forms import EmpForm,FeedbackForm
# Create your views here

def employee(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{'emps':emps})

def add_emp(request):
    if request.method=="POST":
        print('data is comming')
    #data fetch
        emp_name=request.POST.get('emp_name')
        emp_id=request.POST.get('emp_id')
        emp_address=request.POST.get('emp_address')
        emp_phone=request.POST.get('emp_phone')
        emp_working=request.POST.get('emp_working')
        emp_department=request.POST.get('emp_department')
        # Validtion

        #Create Model Object and set data

        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.working=emp_working
        e.department=emp_department 
        
        if emp_working is None:
            e.working=False
        else:
            e.working=True
            # save the object

        e.save()
        #prepare msg

        return redirect('/emp/home') 
    form=EmpForm
    return render(request,'emp/add_emp.html',{'form':form}) 
def delete_emp(request,emp_id):
    print(emp_id)
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect('/emp/home/')

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{'emp':emp})


def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get('emp_name')
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        e=Emp.objects.get(pk=emp_id)
        print(emp_id_temp)
        print(emp_name)
        e.name = emp_name
        e.emp_id = emp_id_temp 
        e.phone = emp_phone
        e.address = emp_address
        # e.working = emp_working
        e.department= emp_department
        print(e.name)
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        # Save the object 
        
        e.save()
    return redirect('/emp/home/')


def testimonials(request):
    testi=Testimonial.objects.all()
    return render(request,"emp/testimonials.html",{'testi':testi})

def feedback(request):
    forms=Feedback.objects.all()
    return render(request,'emp/feedback.html',{'form':forms})
