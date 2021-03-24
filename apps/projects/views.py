from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project, Criteria
from .serializer import ProjectSerializer, CriteriaSerializer
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView, View


def index(request):
    return render(request, "projects/index.html")


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "name", "responsible"]


class CriteriaViewSet(ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer


class ProjectsOutputView(LoginRequiredMixin, View):
    """cписок заявок"""

    def get(self, request, pk=None):
        project = None
        project = Project.objects.all()
        return render(
            request, "projects/projects_output.html", context={"project": project},
        )


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """создание проекта"""

    model = Project
    template_name = "projects/project_create.html"
    form_class = forms.ProjectCreateForm
    success_url = reverse_lazy("projects_output_url")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
