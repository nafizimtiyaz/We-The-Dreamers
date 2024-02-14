import uuid
from django.db import models
from django.utils.text import slugify


class Wings(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class WorkDescription(models.Model):
    wings = models.ForeignKey(Wings, on_delete=models.CASCADE)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='wings/image')
    description = models.TextField(max_length=500)
    image2 = models.ImageField(upload_to='wings/image', null=True, blank=True)
    image3 = models.ImageField(upload_to='wings/image', null=True, blank=True)
    description2 = models.TextField(max_length=1000)
