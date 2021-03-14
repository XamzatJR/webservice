from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BooleanField, CharField, EmailField
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = EmailField(
        ("email address"),
        unique=True,
        error_messages={"unique": _("Такой email уже зарегистрирован")},
    )
    is_expert = BooleanField(_("Is expert"), default=False)
    middle_name = CharField(_("Middle name"), max_length=150, blank=True)
    objects = CustomUserManager()

    def __str__(self):
        return self.username
