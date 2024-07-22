from django.contrib.auth.models import AbstractUser
from django.db import models

from network.models import Network


class User(AbstractUser):
    """Creating User model inherit only from AbstractUser"""
    username = None  # turn off login through username
    email = models.EmailField(unique=True, verbose_name='email')
    # user's network to connect to any network as employee
    network = models.ForeignKey(Network, on_delete=models.CASCADE, null=True, blank=True, related_name='employees',
                                verbose_name='Network')

    USERNAME_FIELD = "email"  # through what log in
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
