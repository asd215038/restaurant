from django.contrib import admin
from .models import Origins, Origins_Food, Processing_Plant, Product, Booking
# Register your models here.

admin.site.register(Origins)  
admin.site.register(Origins_Food)
admin.site.register(Processing_Plant)
admin.site.register(Product)
admin.site.register(Booking)