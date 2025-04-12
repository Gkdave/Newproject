from django.contrib import admin
from .models import Emp,Testimonial,Feedback 
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id','phone')
    list_editable=('working','emp_id')
    search_fields=('name',)
    list_filter=('working',)
    list_per_page=4


admin.site.register(Emp,EmpAdmin)