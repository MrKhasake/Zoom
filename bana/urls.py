from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entrepreneur/', views.entrepreneur, name='entrepreneur'),
    path('sales/', views.sales, name='sales'),
    path('finance/', views.finance, name='finance'),
    path('contact/', views.contact, name='contact')
]