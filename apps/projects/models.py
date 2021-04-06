from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import (
    BooleanField,
    CharField,
    DateTimeField,
    TextField,
    URLField,
    IntegerField,
)
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _

from random import randint


def random_hex() -> str:
    return "#" + str(hex(randint(0, 16777215)))[2:]


class Project(models.Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, db_index=True)
    name = CharField(_("Название проекта"), max_length=150, db_index=True)
    site = URLField(_("Ссылка на сайт проекта"), max_length=200)
    description = TextField(_("Описание продукта/сервиса"))
    note = CharField(_("Примечание к проекту"), max_length=150)
    responsible = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name="responsible",
        verbose_name=_("Ответственный"),
        db_index=True,
        blank=True,
        null=True,
    )
    created_at = DateTimeField(_("Время создания"), auto_now_add=True)
    hex_color = CharField(_("Hex цвет"), max_length=20, default=random_hex())
    science = IntegerField(_("Наука"), default=0)
    interesting = IntegerField(_("Интересный"), default=0)
    difficult = IntegerField(_("Сложный"), default=0)
    unclear = IntegerField(_("Непонятный"), default=0)
    repeat = IntegerField(_("Повтор"), default=0)
    rating = IntegerField(_("Рейтинг"), default=0)

    def __str__(self):
        return self.name


class Criteria(models.Model):
    app = ForeignKey(Project, on_delete=CASCADE, db_index=True)
    expert = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, db_index=True)
    science = BooleanField(_("Есть наука"), default=False)
    interesting = BooleanField(_("Интересный"), default=False)
    difficult = BooleanField(_("Сложный"), default=False)
    unclear = BooleanField(_("Непонятный"), default=False)
    repeat = BooleanField(_("Повтор"), default=False)

    def __str__(self):
        return self.app.name

    def save(
        self, force_insert=None, force_update=None, using=None, update_fields=None
    ) -> None:
        if update_fields:
            self.app.__dict__[update_fields[0]] += (
                1 if self.__dict__[update_fields[0]] else -1
            )
        if update_fields[0] in ["science", "interesting"]:
            self.app.rating += 1
        else:
            self.app.rating -= 1
        self.app.save()
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
