from rest_framework import serializers
from emp.models import Emp 

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'
        