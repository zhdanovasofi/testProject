from django.conf.urls import include, url
from . import views
from django.urls import path,re_path

urlpatterns = [
    path('', views.main, name='main'),
    path('categories/', views.categories, name = 'categories'),
    path('products/', views.products, name = 'products'),
    path('products/choice/', views.choice),
    path('registration/',RegisterFormView.as_view(),name = 'registration'),
    path('authorization/', views.authorization, name = 'authorization')
]
