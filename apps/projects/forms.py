from django import forms

from .models import Criteria, Project


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
