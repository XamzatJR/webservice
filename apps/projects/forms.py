from django import forms
from django.db import models
from django.db.models import fields

from .models import Criteria, NiokrUser, Project, NiokrProject, NiokrCriteria


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "site", "description", "note", "cover")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "cover", "site", "description", "note")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class ProjectAddResponsibleForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("responsible",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class CriteriaForm(forms.ModelForm):
    class Meta:
        model = Criteria
        fields = ("science", "interesting", "difficult", "unclear", "repeat")


class NiokrProjectCreateForm(forms.ModelForm):
    class Meta:
        model = NiokrProject
        fields = (
            "theme",
            "site",
            "data_project_start",
            "base_organisation",
            "science_novelty",
            "commercial_result",
            "equipment",
            "grants",
            "patents",
            "cover",
            "annotation",
            "responsible",
            "team",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class NiokrProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = NiokrProject
        fields = (
            "theme",
            "site",
            "data_project_start",
            "base_organisation",
            "science_novelty",
            "commercial_result",
            "equipment",
            "grants",
            "patents",
            "cover",
            "annotation",
            "responsible",
            "team",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class NiokrCriteriaForm(forms.ModelForm):
    class Meta:
        model = NiokrCriteria
        fields = ("science", "interesting", "difficult", "unclear", "repeat")


class NiokrUserCreate(forms.ModelForm):
    class Meta:
        model = NiokrUser
        fields = (
            "fullname",
            "phone",
            "email",
            "academic_degrees",
            "academic_titles",
            "photo",
        )
