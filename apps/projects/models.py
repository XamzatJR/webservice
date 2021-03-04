from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings

from django.db.models.fields import (
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    EmailField,
    IntegerField,
    PositiveIntegerField,
    TextField,
    URLField,
)
from django.db.models.fields.related import ForeignKey
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)

    data_create = DateTimeField(_("Время создания"), auto_now_add=True)

    project_name = CharField(_("Название проекта"), max_length=150, db_index=True)

    project_site = URLField(_("Ссылка на сайт проекта"), max_length=200)

    project_description = TextField(_("Описание продукта/сервиса"))

    project_note = CharField(_("Примечание к проекту"), max_length=150, db_index=True)

    project_responsible = CharField(_("Ответственный"), max_length=150, db_index=True)
