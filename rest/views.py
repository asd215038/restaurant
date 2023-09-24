from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Booking
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your views here.
def index(request):
    return render(request, 'base.html')  

# new_record = Booking.objects.create(booking_time=timezone.now() + timezone.timedelta(hours=1))

#當訂位時間
# @receiver(pre_delete, sender=Booking)
# def delete_record(sender, instance, **kwargs):
#     if instance.booking_time <= timezone.now():
#         instance.delete()