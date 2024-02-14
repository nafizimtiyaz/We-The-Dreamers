from django.contrib import admin
from django.urls import path
from AboutUs import views #about_us_detail

urlpatterns = [
    path('about', views.AboutView, name='about'),
    # path('about-us/<uuid:uid>/', views.about_us_detail, name='about_us_detail'),
]
