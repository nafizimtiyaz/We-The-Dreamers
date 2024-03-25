import uuid
from django.db import models
from ckeditor.fields import RichTextField


class AboutUs(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    description = RichTextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to='about/us')


class OurMission(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    description = RichTextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to='about/us/mission')


class OurVision(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    description = RichTextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to='about/us/vision')


class AboutActivity(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    image = models.ImageField(upload_to='about/us/vision')
    description = models.TextField(max_length=4000)
    name = RichTextField(max_length=10000, null=True, blank=True)


class MedicalWings(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    description = RichTextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to='wing/medical', null=True, blank=True)


class EducationWing(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    description = RichTextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to='wing/Education', null=True, blank=True)


class DisasterManagementWig(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    description = RichTextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to='wing/Disaster', null=True, blank=True)


class Review(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    image = models.ImageField(upload_to='Review')
    name = models.CharField(max_length=200)
    description = RichTextField(max_length=10000, null=True, blank=True)
