from django.db import models
from django.urls import reverse

# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Branch(models.Model):
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Userform(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.IntegerField()
    phonenumber=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    district=models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch=models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name