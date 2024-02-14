import uuid
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Slider(models.Model):
    image = models.ImageField(upload_to='home/slider')
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=200)


class Category(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class OurActivity(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recent/activity')
    description = RichTextField(max_length=1000, null=True, blank=True)
    image2 = models.ImageField(upload_to='recent/activity', null=True, blank=True)
    image3 = models.ImageField(upload_to='recent/activity', null=True, blank=True)
    description2 = RichTextField(max_length=1000, null=True, blank=True)


class Event(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recent/activity')
    description = RichTextField(max_length=1000, null=True, blank=True)
    date = models.DateField()
    time = models.CharField(max_length=12)
