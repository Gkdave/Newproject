from django.contrib import admin
from .models import Emp,Testimonial,Feedback 
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','department','sallary','phone')
    list_editable=('sallary','phone')
    search_fields=('name',)
    list_filter=('department',)
    list_per_page=4


admin.site.register(Emp,EmpAdmin)
# admin.site.register(Emp)
admin.site.register(Testimonial)
admin.site.register(Feedback)