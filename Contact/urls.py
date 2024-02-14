from django.contrib import admin
from django.urls import path
from Contact import views

urlpatterns = [
    path('contact', views.ContactUs, name='contact'),
]