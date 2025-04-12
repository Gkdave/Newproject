from django.urls import path 
from .views import * 

urlpatterns = [
    path('home/',employee,name='emp'),
    path('add-emp/',add_emp),
    path('delete-emp/<int:emp_id>/',delete_emp),
    path('update-emp/<int:emp_id>/',update_emp),
    path('do-update-emp/<int:emp_id>',do_update_emp),
    path('testimonials/',testimonials),
    path('feedback/',feedback),
    path('do-feedback/',do_feedback),
    path('delete-feedback/<int:id>/',delete_feedback),

]
