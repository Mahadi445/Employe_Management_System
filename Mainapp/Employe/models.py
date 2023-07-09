from django.db import models
from django.utils import timezone
from Department.models import Department
from Position.models import Position


# Create your models here.

class Employees(models.Model):
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    ]
        
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100, blank=True) 
    firstname = models.CharField(max_length=100) 
    lastname = models.CharField(max_length=100) 
    gender =models.CharField(max_length=10, choices=GENDER_CHOICES, default='Others')
    dob = models.DateField(blank=True, null=True) 
    contact = models.CharField(max_length=25) 
    address = models.TextField() 
    email = models.EmailField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField(blank=True, null=True) 
    salary = models.FloatField(default=0) 
    status = models.BooleanField()
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.firstname}  {self.lastname}"
    
    
    