from rest_framework import serializers

from .models import Project, Criteria, NiokrCriteria, NiokrProject


class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    responsible = serializers.SlugRelatedField(read_only=True, slug_field="username")
    photo = serializers.SerializerMethodField("get_photo_url")
    cover = serializers.SerializerMethodField("get_cover_url")

    class Meta:
        model = Project
        fields = (
            "pk",
            "name",
            "user",
            "photo",
            "cover",
            "site",
            "description",
            "note",
            "responsible",
            "created_at",
            "hex_color",
            "rating",
            "science",
            "interesting",
            "difficult",
            "unclear",
            "repeat",
            "rating",
        )

    def get_photo_url(self, obj):
        try:
            return obj.photo.url
        except Exception:
            return ""

    def get_cover_url(self, obj):
        try:
            return obj.cover.url or "none"
        except Exception:
            return ""


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


class NiokrProjectSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    responsible = serializers.SlugRelatedField(read_only=True, slug_field="username")
    photo = serializers.SerializerMethodField("get_photo_url")
    cover = serializers.SerializerMethodField("get_cover_url")

    class Meta:
        model = NiokrProject
        fields = (
            "pk",
            "user",
            "theme",
            "photo",
            "data_project_start",
            "base_organisation",
            "science_novelty",
            "commercial_result",
            "equipment",
            "grants",
            "patents",
            "cover",
            "annotation",
            "niokr_responsible",
            "created_at",
            "hex_color",
            "rating",
            "science",
            "interesting",
            "difficult",
            "unclear",
            "repeat",
            "rating",
        )

    def get_photo_url(self, obj):
        try:
            return obj.user.photo.url
        except Exception:
            return ""

    def get_cover_url(self, obj):
        try:
            return obj.cover.url or "none"
        except Exception:
            return ""


class NiokrCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NiokrCriteria
        fields = (
            "app",
            "expert",
            "science",
            "interesting",
            "difficult",
            "unclear",
            "repeat",
        )
