from django.contrib import admin
from django.urls import path
from AboutUs import views #about_us_detail

urlpatterns = [
    path('about', views.AboutView, name='about'),
    path('wings/medical',views.medical_wings,name='medical'),
    path('wings/education',views.education_wings,name='education'),
    path('wings/Disaster-Management',views.disaster_wings,name='disaster'),
]
