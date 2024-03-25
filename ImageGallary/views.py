from django.shortcuts import render
from .models import Category, Gallery
from Home import models


def image_gallary(request):
    image = Category.objects.all()
    all_images = Gallery.objects.all()
    cat = models.Category.objects.all()

    return render(request, 'gallery.html', {'cat': cat,'image':image,'all_images': all_images})
