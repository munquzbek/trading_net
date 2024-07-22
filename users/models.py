from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import BaseUserManager

from network.models import Network


class CustomUserManager(BaseUserManager):
    """this class defines methods for creating users and superusers."""
    def create_user(self, email, password=None, **extra_fields):
        """designed to create regular users"""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """designed to create superusers"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Creating User model inherit only from AbstractUser"""
    username = None  # turn off login through username
    email = models.EmailField(unique=True, verbose_name='email')
    # user's network to connect to any network as employee
    network = models.ForeignKey(Network, on_delete=models.CASCADE, null=True, blank=True, related_name='employees',
                                verbose_name='Network')

    USERNAME_FIELD = "email"  # through what log in
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
