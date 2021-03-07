from rest_framework import serializers
from .models import Project
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


class ProjectSerializer(serializers.Serializer):
    data_create = serializers.DateTimeField()

    project_name = serializers.CharField(max_length=150,)

    project_site = serializers.URLField(max_length=200)

    project_description = serializers.CharField()

    project_note = serializers.CharField(max_length=150,)

    project_responsible = serializers.CharField(max_length=150,)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.project_name = validated_data.get(
            "project_name", instance.project_name
        )
        instance.project_description = validated_data.get(
            "project_description", instance.project_description
        )
        instance.project_note = validated_data.get(
            "project_note", instance.project_note
        )
        instance.project_responsible = validated_data.get(
            "project_responsible", instance.project_responsible
        )

        instance.save()
        return instance
