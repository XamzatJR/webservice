from django import forms

from .models import Criteria, Project, NiokrProject, NiokrCriteria


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
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class NiokrCriteriaForm(forms.ModelForm):
    class Meta:
        model = NiokrCriteria
        fields = ("science", "interesting", "difficult", "unclear", "repeat")
