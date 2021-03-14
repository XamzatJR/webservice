from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings

from django.db.models.fields import (
    CharField,
    BooleanField,
    DateTimeField,
    TextField,
    URLField,
)
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import post_save
from django.dispatch import receiver


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
        limit_choices_to={"is_expert": True, "is_active": True},
        db_index=True,
    )
    created_at = DateTimeField(_("Время создания"), auto_now_add=True)

    def __str__(self):
        return self.name


class Criteria(models.Model):
    app = ForeignKey(Project, on_delete=CASCADE)
    science = BooleanField(_("Есть наука"), default=False)
    interesting = BooleanField(_("Интересный"), default=False)
    difficult = BooleanField(_("Сложный"), default=False)
    unclear = BooleanField(_("Непонятный"), default=False)
    repeat = BooleanField(_("Повтор"), default=False)

    def __str__(self):
        return self.app.name


@receiver(post_save, sender=Project)
def create_criteria(sender, instance, created, **kwargs):
    Criteria.objects.create(app=instance)


@receiver(post_save, sender=Project)
def save_criteria(sender, instance, **kwargs):
    instance.Criteria.save()
