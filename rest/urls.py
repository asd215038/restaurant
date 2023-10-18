from django.urls import path
from . import views  #引用這個資料夾中的views檔案

urlpatterns = [
    path('', views.homepage),
    path('menu', views.menu),
    path('ingredients', views.ingredients),
    path('booking', views.booking),
    path('menu/management', views.menu_mangament),
    path('menu/origins/new', views.origins_new),
    path('menu/origins-food/new', views.origins_food_new),
    path('menu/processing-plant/new', views.processing_plant_new),
    path('menu/product/new', views.product_new),

]