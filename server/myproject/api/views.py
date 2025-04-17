from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from rest_framework import status 
from emp.models import Emp 
from .serializers import EmployeeSerializer 


# Create your views here.
@api_view(['GET','POST'])
def employee_List(request):
    if request.method=='GET':
        employees=Emp.objects.all()
        serializer=EmployeeSerializer(employees,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def employee_detail(request,pk):
    try:
        employee=Emp.objects.get(pk=pk)
    except Emp.DoesNotExist:
        return Response({'error':"Emp not found"},status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=EmployeeSerializer(employee,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        employee.delete()
        return Response({'message':"Employee deleted"},status=status.HTTP_204_NO_CONTENT)
    