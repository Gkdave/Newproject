from django.urls import path 
from .views import employee_List,employee_detail
urlpatterns = [
    path('employees/',employee_List),
    path('employees/<int:pk>/',employee_detail),
]
