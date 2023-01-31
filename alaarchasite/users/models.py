from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, help_text="Enter you email", blank=False, unique=True)
    phone_number = PhoneNumberField(
        verbose_name="Номер телефона",
        null=False,
        blank=False,
        unique=True,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'password']
    objects = CustomUserManager()

    def __str__(self):
        return self.email
