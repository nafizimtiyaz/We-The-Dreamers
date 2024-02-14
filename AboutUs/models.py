import uuid
from django.db import models


class AboutUs(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/us')


class OurMission(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/us/mission')


class OurVision(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/us/vision')


class AboutActivity(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    image = models.ImageField(upload_to='about/us/vision')
    description = models.TextField(max_length=4000)
    name = models.TextField(max_length=200)


class MedicalWings(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=4000)


class EducationWing(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=4000)


class DisasterManagementWig(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=4000)
