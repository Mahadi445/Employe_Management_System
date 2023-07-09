from django.db import models
from django.utils import timezone
# Create your models here.

class Position(models.Model):
    id =models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=250, default=0)
    description = models.TextField() 
    status = models.BooleanField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.position_name