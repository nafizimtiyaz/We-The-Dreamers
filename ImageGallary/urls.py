from django.contrib import admin
from django.urls import path
from ImageGallary import views

urlpatterns = [
    path('gallery', views.image_gallary, name='gallery'),
]