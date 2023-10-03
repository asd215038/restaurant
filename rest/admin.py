from django.contrib import admin
from .models import Origins, Origins_Food, Processing_Plant, Product, Booking
# Register your models here.

class OriginsAdmin(admin.ModelAdmin):
    list_display = ('photo', 'name')

class Origins_FoodAdmin(admin.ModelAdmin):
    list_display = ('photo', 'name', 'produce_from', 'price')

class Processing_PlantAdmin(admin.ModelAdmin):
    list_display = ('photo', 'name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('photo', 'name', 'produce_from', 'price')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_people', 'phone_number', 'booking_time', 'create_date')

admin.site.register(Origins, OriginsAdmin)  
admin.site.register(Origins_Food, Origins_FoodAdmin)
admin.site.register(Processing_Plant, Processing_PlantAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Booking, BookingAdmin)