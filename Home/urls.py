from django.contrib import admin
from django.urls import path
from Home import views
from core.views import add_volunteer

urlpatterns = [
    path('', views.Home, name='home'),
    path('events', views.event_list, name='events'),
    path('category/<slug:slug>', views.category_detail, name='category_detail'),
    path('volunteer/form', add_volunteer, name='volunteer'),
]

