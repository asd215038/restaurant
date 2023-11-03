from django import forms
from .models import Booking, Origins, Origins_Food, Processing_Plant, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OriginsModelForm(forms.ModelForm):

    class Meta:
        model = Origins
        fields = ['photo', 'name']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'photo' : '選擇圖片',
            'name': '輸入名稱',

        }

        photo = forms.ImageField()

class Origins_FoodModelForm(forms.ModelForm):
    produce_from = forms.ModelChoiceField(queryset=Origins.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Origins_Food
        fields = ['photo', 'name', 'produce_from', 'price']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'photo' : '選擇圖片',
            'name': '輸入名稱',
            'produce_from': '原產地',
            'price': '輸入價格',

        }


class Processing_PlantModelForm(forms.ModelForm):

    class Meta:
        model = Processing_Plant
        fields = ['photo', 'name']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'photo' : '選擇圖片',
            'name': '輸入名稱',

        }

class ProductModelForm(forms.ModelForm):
    produce_from = forms.ModelChoiceField(queryset=Processing_Plant.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        fields = ['photo', 'name', 'produce_from', 'price']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'photo' : '選擇圖片',
            'name': '輸入名稱',
            'produce_from': '原產地',
            'price': '輸入價格',

        }

