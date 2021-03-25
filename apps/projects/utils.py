from django.shortcuts import get_object_or_404, redirect, render

from apps.projects import forms, models


class ObjectDetailMixin:
    """миксин для обзора проекта"""

    model = models.Project
    template_name = "projects/project_detail.html"

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        return render(request, self.template_name, context={"project": obj,},)
