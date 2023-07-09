from django.db import models
from django.utils import timezone

# Create your models here.

class Department(models.Model):
    id =models.AutoField(primary_key=True)
    depart_name = models.CharField(max_length=250)
    description = models.TextField()
    status = models.BooleanField()
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.depart_name
    
    
    
    
    
