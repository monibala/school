from email.message import Message
from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_number = models.IntegerField()
    
class contact(models.Model):
    Name = models.CharField(max_length=100)    
    Email = models.EmailField()
    Mobile_Number = models.IntegerField()
    Message = models.TextField()