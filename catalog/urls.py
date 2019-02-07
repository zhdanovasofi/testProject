from django.conf.urls import url
from . import views
from django.urls import path,re_path

urlpatterns = [
    path('', views.main, name='main'),
    path('categories/', views.categories, name = 'categories'),
    path('products/', views.products, name = 'products'),
    path('products/choice/', views.choice)
]
