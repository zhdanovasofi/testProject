from django.shortcuts import render, redirect
from .models import Product, Category
import datetime
from django.shortcuts import render_to_response

def main(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    return render(
        request,
        'main.html'
    )

def categories(request):
    categoriesList = Category.objects.all()
    return render(
    request,
    'categories.html',
    {'categoriesList': categoriesList }
    )

def products(request):
    productsList  = Product.objects.filter()
