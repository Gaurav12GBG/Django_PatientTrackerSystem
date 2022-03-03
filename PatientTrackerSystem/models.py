from datetime import datetime
from django.db import models

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=250, null=True)
     
    def __str__(self):
        return self.email
    
class PatientInfo(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    adharno = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    dob = models.DateField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    maritalstatus = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    taluka = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    diabetes = models.CharField(max_length=100)
    cancer = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=100)
    diseases = models.CharField(max_length=100)
    vaccinestatus = models.CharField(max_length=100)
    datetime = models.DateField(max_length=30, auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return f"{self.fname} {self.mname} {self.lname}"

    
