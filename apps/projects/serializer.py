from rest_framework import serializers

from .models import Project, Criteria


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("user", "name", "site", "description", "note", "responsible")


class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = (
            "app",
            "expert",
            "science",
            "interesting",
            "difficult",
            "unclear",
            "repeat",
        )
