from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.IntegerField()
    phone=models.BigIntergerField()
    address=models.CharField(max_length=200)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=200)

    def __str__(self):
        return self.name + self.department 
    
class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    Testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonials")
    rating=models.IntegerField(null=True)

    def __str__(self):
        return self.name 
    
class Feedback(models.Model):
    email=models.EmailField(max_length=200)
    name=models.CharField(max_length=100)
    feedback=models.TextField()

    def __str__(self):
        return self.name + self.email 
