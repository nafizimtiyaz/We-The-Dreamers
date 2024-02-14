from django.contrib import admin
from .models import Slider, Category, OurActivity,Event


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(OurActivity)
class OurActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title',)


@admin.register(Event)
class EnevtAdmin(admin.ModelAdmin):
    list_display = ['uid', 'title', 'date', 'time', 'image']
    readonly_fields = ['uid']
    search_fields = ['title', 'description']

