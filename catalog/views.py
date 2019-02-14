from django.shortcuts import render, redirect
from .models import Product, Category
import datetime
from django.shortcuts import render_to_response
from .forms import RegisterFormView
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
    productsList  = Product.objects.filter(balance__gte = 1).order_by('product_price')
    categories = Category.objects.all()
    return render(
    request,
    'products.html',
    {'productsList': productsList, 'categories':categories }
    )
def choice(request):
    categories = Category.objects.all()
    category = request.POST.get('categ')
    categoryID = Category.objects.filter(category_name = category).values('categoty_id').distinct()
    if category == 'all':
        category = 'все'
        productsList  = Product.objects.filter(balance__gte = 1).order_by('product_price')
        return render(
                request,
                'productsfromcategories.html',
                {'productsList': productsList, 'category': category }
            )
    else:
            #categoryID = Category.objects.filter(category_name = category).values('category_id').distinct()
        productsList  = Product.objects.filter(balance__gte = 1, categoty_id__in = categoryID).order_by('product_price')
        return render(
                request,
                'productsfromcategories.html',
                {'productsList': productsList, 'category': category }
                )
