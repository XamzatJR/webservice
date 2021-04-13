from django.contrib.auth.models import AbstractUser
from django.db.models import Model
from django.db.models.fields import BooleanField, CharField, EmailField
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = EmailField(
        ("E-mail"),
        unique=True,
        error_messages={"unique": _("Такой email уже зарегистрирован")},
    )
    is_expert = BooleanField(_("Статус эксперта"), default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class InviteCode(Model):
    code = CharField(_("Код"), max_length=100)

    @staticmethod
    def get_or_none(*args, **kwargs):
        try:
            return InviteCode.objects.get(*args, **kwargs)
        except InviteCode.DoesNotExist:
            return None
