import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Create and save a new User with the given email and password
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Create and save a new superuser with the given email and password
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=16, null=True, blank=True)
    present_address = models.TextField(max_length=1000, null=True, blank=True)
    profession = models.TextField(max_length=1000, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_full_name(self):
        # Return the full name of the user
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        # Return the short name of the user
        return self.first_name


class Volunteer(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    volunteer_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_of_birth = models.CharField(max_length=20)
    permanentAddress = models.TextField(max_length=1000)
    present_address = models.TextField(max_length=1000)
    profession = models.CharField(max_length=100)
    running_degree = models.TextField(max_length=400, null=True, blank=True)
    leftest_degree = models.TextField(max_length=400, null=True, blank=True)
    passing_year = models.CharField(max_length=100, null=True, blank=True)
    institute = models.TextField(max_length=400, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    other_description = models.TextField(max_length=400, null=True, blank=True)
    blood_group = models.CharField(max_length=100)
    previous_organization = models.CharField(max_length=100,null=True, blank=True)
    organization_duty = models.TextField(max_length=100, null=True, blank=True)
    present_organization = models.CharField(max_length=100, null=True, blank=True)
    interested_charity_work = models.TextField(max_length=3000)

