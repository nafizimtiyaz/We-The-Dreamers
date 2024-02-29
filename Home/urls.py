from django.contrib import admin
from django.urls import path
from Home import views
from core.views import add_volunteer

urlpatterns = [
    path('', views.Home, name='home'),
    path('events', views.event_list, name='events'),
    path('events/<uuid:uid>', views.event_detail, name='event-detailss'),
    path('category/<slug:slug>', views.category_detail, name='category_detail'),
    path('volunteer/form', add_volunteer, name='volunteer'),
    path('book-camp', views.medical_camp, name='camp'),
    path('recent/activity', views.recent_activaties,name='all'),
    path('recent/activity/<uuid:uid>', views.activity_details, name='details'),

]

