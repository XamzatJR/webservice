from django import forms

from .models import Criteria, NiokrUser, Project, NiokrProject, NiokrCriteria


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "site", "description", "tag", "note", "cover")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "cover", "site", "tag", "description", "note")

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
        widgets = {
            "data_project_start": forms.DateInput(
                format=("%d-%m-%Y"), attrs={"placeholder": "Выберите дату"},
            )
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["responsible"].queryset = NiokrUser.objects.filter(
            user=user, is_responsible=True
        )
        self.fields["team"].queryset = NiokrUser.objects.filter(
            user=user, is_responsible=False
        )
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

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["responsible"].queryset = NiokrUser.objects.filter(
            user=user, is_responsible=True
        )
        self.fields["team"].queryset = NiokrUser.objects.filter(
            user=user, is_responsible=False
        )
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
            "is_responsible",
            "ec_id",
            "photo",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == "is_responsible":
                continue
            self.fields[field].widget.attrs["class"] = "form-control"
