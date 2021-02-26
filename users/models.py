from io import BytesIO
from pathlib import Path

from django.contrib.auth.models import AbstractUser
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.fields import BooleanField, CharField, EmailField
from django.db.models.fields.related import OneToOneField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """Кастомная модель пользователей"""

    email = EmailField(
        ("email address"),
        unique=True,
        error_messages={"unique": _("Такой email уже зарегистрирован")},
    )
    is_expert = BooleanField(_("Статус эксперта"), default=False)
    middle_name = CharField(_("Отчество"), max_length=150, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
