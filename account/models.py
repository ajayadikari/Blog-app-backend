from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import AccountManager


class AccountModel(AbstractUser, PermissionsMixin):

    gender_choices = [
        ('m', 'male'), 
        ('f', 'female')
    ]

    contact = models.IntegerField(unique=True, null=True, blank=True)
    gender = models.CharField(choices=gender_choices, blank=False, null=False, default='m', max_length=10)
    address = models.TextField(null=True, blank=True)
    is_author = models.BooleanField(default=False)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    imageUrl = models.TextField(null=True, blank=True)

    # USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = AccountManager()