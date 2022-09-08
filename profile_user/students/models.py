from django.db import models


# Create your models here.

class Register(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Email_Id=models.CharField(max_length=50)
    Department_Name=models.CharField(max_length=50)
    Section_Name=models.CharField(max_length=26)
    Phone_Number=models.CharField(max_length=10)
    Roll_Number=models.CharField(max_length=100) 

    
    


