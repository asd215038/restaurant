from django.db import models
from django.utils import timezone

#原產地
class Origins(models.Model):
    name = models.CharField(max_length=50)

#原料
class Origins_Food(models.Model):
    name = models.CharField(max_length=50)  #品名
    produce_from = models.ForeignKey(Origins, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()  #價格

#加工廠
class Processing_Plant(models.Model):
    name = models.CharField(max_length=50)
    
#產品
class Product(models.Model):
    name = models.CharField(max_length=50)  #品名
    produce_from = models.ForeignKey(Processing_Plant, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()  #價格
    
#訂位紀錄
class Booking(models.Model):
    name = models.CharField(max_length=50)  #品名
    number_of_people = models.IntegerField()  #價格
    phone_number = models.IntegerField()  #價格
    booking_time = models.DateField(default=timezone.now)  #貼文時間
    create_date = models.DateField(default=timezone.now)  #貼文時間
    