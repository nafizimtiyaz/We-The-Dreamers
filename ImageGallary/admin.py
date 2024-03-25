from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Gallery,Category


class GalleryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
    list_filter = ('category',)


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category)
