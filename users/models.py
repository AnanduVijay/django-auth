from django.db import models

from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):

    username = None
    email = models.EmailField(_("emailaddress"), unique=True)
    phone_no = models.IntegerField(_("phone_no"), unique=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

