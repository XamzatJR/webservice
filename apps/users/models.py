from django.contrib.auth.models import AbstractUser
from django.db.models import Model
from django.db.models.fields import BooleanField, CharField, EmailField, URLField
from django.utils.translation import gettext_lazy as _
from django.db.models import ImageField
from .managers import CustomUserManager
from django.shortcuts import reverse


class CustomUser(AbstractUser):
    email = EmailField(
        ("E-mail"),
        unique=True,
        error_messages={"unique": _("Такой email уже зарегистрирован")},
    )
    is_expert = BooleanField(_("Статус эксперта"), default=False)

    photo = ImageField(
        _("Фото профиля"), upload_to="avatar_photos/", null=True, blank=True
    )

    url = URLField(_("Ссылка на фото"), null=True, blank=True)
    
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def get_update_url(self):
        return reverse("photo_update_url", kwargs={"pk": self.pk})


class InviteCode(Model):
    code = CharField(_("Код"), max_length=100)

    @staticmethod
    def get_or_none(*args, **kwargs):
        try:
            return InviteCode.objects.get(*args, **kwargs)
        except InviteCode.DoesNotExist:
            return None
