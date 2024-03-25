from django.contrib import admin
from .models import AboutUs, OurMission, OurVision, AboutActivity, MedicalWings, EducationWing, DisasterManagementWig, \
    Review


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title', 'description',)


@admin.register(OurMission)
class OurMissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title', 'description',)


@admin.register(OurVision)
class OurVisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title', 'description',)


@admin.register(AboutActivity)
class AboutActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(MedicalWings)
class MedicalWingsAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)


@admin.register(EducationWing)
class EducationWingAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)


@admin.register(DisasterManagementWig)
class DisasterManagementWigAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)


@admin.register(Review)
class EnevtAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
