from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from myapp.manager import CustomUserManager


class Customuser(AbstractUser):
    """
    This class store the users data.
    """

    username = None
    email = models.EmailField(_("email address"), unique=True)
    is_verify = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
