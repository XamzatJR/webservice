from rest_framework import serializers

from .models import Project, Criteria


class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Project
        fields = (
            "pk",
            "name",
            "user",
            "site",
            "description",
            "note",
            "responsible",
            "hex_color",
            "rating",
            "photo",
            "cover",
        )


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
