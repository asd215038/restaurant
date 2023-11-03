from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Booking, Origins, Origins_Food, Processing_Plant, Product
from .forms import OriginsModelForm, Origins_FoodModelForm, Processing_PlantModelForm, ProductModelForm
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
from django.contrib import messages

# Create your views here.
def homepage(request):
    photos_folder = 'static/image'  # 資料夾路徑
    photos = [os.path.join(photos_folder, filename) for filename in os.listdir(photos_folder) if filename.endswith('.png')]
    return render(request, 'homepage.html', locals())

def menu(request):
    
    return render(request, 'menu.html', locals())

def origins_new(request):
    form = OriginsModelForm()
    if request.method == "POST":
        form = OriginsModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '新增成功')
            return redirect('/menu/management')
    return render(request, 'menu/origins_new.html', locals())

def origins_food_new(request):
    origins = Origins.objects.all()
    form = Origins_FoodModelForm()
    if request.method == "POST":
        form = Origins_FoodModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '新增成功')
            return redirect('/menu/management')
    return render(request, 'menu/origins_food_new.html', locals())

def processing_plant_new(request):
    form = Processing_PlantModelForm()
    if request.method == "POST":
        form = Processing_PlantModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '新增成功')
            return redirect('/menu/management')
    return render(request, 'menu/processing_plant_new.html', locals())

def product_new(request):
    processing_plant = Processing_Plant.objects.all()
    form = ProductModelForm()
    if request.method == "POST":
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '新增成功')
            return redirect('/menu/management')
    return render(request, 'menu/product_new.html', locals())

def menu_mangament(request):
    origins = Origins.objects.all()
    origins_food = Origins_Food.objects.all()
    processing_plant = Processing_Plant.objects.all()
    product = Product.objects.all()

    return render(request, 'menu_mangament.html', locals())

def ingredients(request):
    
    return render(request, 'ingredients.html', locals())

def booking(request):
    
    return render(request, 'booking.html', locals())
