from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import CustomUser, Volunteer


class CustomUserAdmin(UserAdmin):
    search_fields = ['first_name', 'last_name', 'email']  # Enable search by first_name, last_name, and email

    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info',
         {'fields': ('first_name', 'last_name', 'profile_photo', 'phone_number', 'present_address', 'profession')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_of_birth', 'blood_group', 'present_organization')
    search_fields = ('name', 'email', 'blood_group')


admin.site.register(CustomUser, CustomUserAdmin)
