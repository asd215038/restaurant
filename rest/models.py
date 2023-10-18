from django.db import models
from django.utils import timezone

#原產地
class Origins(models.Model):
    photo = models.ImageField(upload_to='origins/', blank=True, default='img.jpg')
    name = models.CharField(max_length=50)

#原料
class Origins_Food(models.Model):
    photo = models.ImageField(upload_to='origins_food/', blank=True, default='img.jpg')
    name = models.CharField(max_length=50)  
    produce_from = models.ForeignKey(Origins, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()

#加工廠
class Processing_Plant(models.Model):
    photo = models.ImageField(upload_to='processing_plant/', blank=True, default='img.jpg')
    name = models.CharField(max_length=50)
    
#產品
class Product(models.Model):
    photo = models.ImageField(upload_to='product/', blank=True, default='img.jpg')
    name = models.CharField(max_length=50)  
    produce_from = models.ForeignKey(Processing_Plant, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()
    
#訂位紀錄
class Booking(models.Model):
    name = models.CharField(max_length=50)  
    number_of_people = models.IntegerField()  
    phone_number = models.IntegerField() 
    booking_time = models.DateField(default=timezone.now)
    create_date = models.DateField(default=timezone.now)
    