from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "user",
            "data_create",
            "project_name",
            "project_site",
            "project_description",
            "project_note",
            "project_responsible",
        )

    def create(self, validated_data):
        project_name = validated_data.pop("project_name")
        project = Project(**validated_data)
        project.save()
        return project
