from django import forms
from .models import Emp,Feedback 

class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Enter your Email",max_length=200)
    name=forms.CharField(label="Enter your name",max_length=100)
    Feedback=forms.CharField(label="Enter your feedback",widget=forms.Textarea)

def __init__(self, *args, **kwargs):
    super(FeedbackForm,self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
        visible.field.widget.attrs['class']='form-control'

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp 
        fields=['name','email','phone','address','sallary','department']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['email','name','feedback'] 
