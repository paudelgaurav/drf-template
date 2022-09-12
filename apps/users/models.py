from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from ..core.models import BaseModel
from ..core.utils.helpers import get_upload_path
from .constants import GENDER_CHOICES
from .manager import UserManager


class User(AbstractUser, BaseModel):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    full_name = models.CharField(_("full name"), max_length=150, blank=True, null=True)

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    # Below fields are optional
    profile_picture = models.ImageField(upload_to=get_upload_path, blank=True)

    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, blank=True, null=True
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.full_name or self.email
