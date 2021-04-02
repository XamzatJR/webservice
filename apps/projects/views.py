from apps.users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from . import forms
from .models import Criteria, Project
from .serializer import CriteriaSerializer, ProjectSerializer


def index(request):
    return render(request, "projects/index.html")


class ProjectsOutputView(LoginRequiredMixin, ListView):
    """cписок всех проектов"""

    model = Project
    template_name = "projects/projects_output.html"
    context_object_name = "project"


class UserProjectsOutputView(LoginRequiredMixin, ListView):
    """cписок своих проектов """

    model = Project
    template_name = "projects/projects_output.html"
    context_object_name = "project"

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """создание проекта"""

    model = Project
    template_name = "projects/project_create.html"
    form_class = forms.ProjectCreateForm
    success_url = reverse_lazy("projects_list_url")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    """обзор проекта"""

    model = Project
    template_name = "projects/project_detail.html"
    success_url = reverse_lazy("project_detail_url")

    def get_context_data(self, **kwargs):
        if self.request.user.is_expert:
            criteria = Criteria.objects.get_or_create(
                app=kwargs["object"], expert=self.request.user
            )
        try:
            kwargs["criteria_form"] = forms.CriteriaForm(instance=criteria[0])
        except UnboundLocalError:
            forms.CriteriaForm

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return super().get_queryset()


class ProjectAddResponsible(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = forms.ProjectAddResponsibleForm
    template_name = "projects/project_add_responsible.html"
    success_url = reverse_lazy("projects_list_url")

    def get_success_url(self):
        return self.success_url


# API Controllers


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "name", "responsible"]


class CriteriaViewSet(ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer


def change_criteria(request):
    if request.is_ajax():
        field = request.GET.get("field")

        user = CustomUser.objects.get(pk=request.GET.get("user"))
        project = Project.objects.get(pk=request.GET.get("project"))
        criteria = Criteria.objects.get(app=project, expert=user)
        criteria.__dict__[field] = not criteria.__dict__[field]
        criteria.save(update_fields=[field])
    return JsonResponse({"code": 200})
