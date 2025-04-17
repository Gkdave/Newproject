
from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200) 
    email=models.EmailField(max_length=254)
    phone=models.BigIntegerField()
    address=models.CharField(max_length=150)
    sallary=models.IntegerField()
    department=models.CharField(max_length=20)

    def __str__(self):
        return self.name + self.department 
    
class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    Testimonial= models.TextField()
    picture=models.ImageField(upload_to="testimonials")
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.name + self.Testimonial
    
class Feedback(models.Model):
    email=models.EmailField(max_length=200)
    name=models.CharField(max_length=200)
    feedback=models.TextField(max_length=200)
    
    def __str__(self):
        return self.name + self.email 
    