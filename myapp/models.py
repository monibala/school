

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    
class Classes(models.Model):
    images = models.ImageField(upload_to='images',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    seats = models.IntegerField(blank=True,null=True)
    time = models.TimeField(blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    fee = models.IntegerField(blank = True, null = True)
    quantity = models.IntegerField(default=1)

   
class Order(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    productid = models.IntegerField(null=True,blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2,null=True)
    total = models.DecimalField(default=0.00,max_digits=100,decimal_places=2,null=True)
    quantity = models.IntegerField(default=1)
    fee = models.IntegerField(blank = True, null = True)

class Checkout(models.Model):
    items = models.ManyToManyField(Order)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    fname = models.CharField(max_length=50,blank=True,null=True)
    lname = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField()
    mob_no = models.IntegerField()
    Address = models.CharField(max_length=200)
    State = models.CharField(max_length=50,blank=True,null=True)
    pincode = models.IntegerField()
class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    item = models.ManyToManyField(Order)
    order_id = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)