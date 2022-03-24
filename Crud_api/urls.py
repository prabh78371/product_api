from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('productapi/',views.product_api,name="api"),
    path('productapi/<int:pk>',views.product_api,name="api")]