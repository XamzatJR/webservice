from itertools import groupby
from operator import attrgetter

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import TruncDate
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django.views.generic.edit import DeleteView, UpdateView

from apps.users.models import CustomUser

from . import forms
from .models import Criteria, Project
from .serializer import CriteriaSerializer, ProjectSerializer


class ProjectsOutputView(LoginRequiredMixin, ListView):
    """cписок всех проектов"""

    model = Project
    template_name = "projects/projects_output.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        users = CustomUser.objects.filter()
        kwargs["users"] = users
        kwargs["experts"] = users.filter(is_expert=True)
        # self.object_list = groupby(self.object_list, attrgetter('created_at_date'))
        return super().get_context_data(**kwargs)

    # def get_queryset(self):
    #     return self.model.objects.annotate(created_at_date=TruncDate('created_at'))


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

class ProjectDeleteView(DeleteView, LoginRequiredMixin):
    """ удаление проекта """

    model = Project
    success_url = reverse_lazy("projects_list_url")
    template_name = "projects/project_delete.html"

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """редактирование проекта"""

    model = Project
    form_class = forms.ProjectUpdateForm
    template_name = "projects/project_update.html"
    success_url = reverse_lazy("projects_list_url")


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
            kwargs["criteria"] = criteria[0]
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
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["user", "responsible"]
    search_fields = ["name"]


class CriteriaViewSet(ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer


def change_criteria(request):
    if request.is_ajax():
        field = request.GET.get("field")
        user = CustomUser.objects.get(pk=request.GET.get("user"))
        if user.is_expert:
            criteria = Criteria.objects.get(app=request.GET.get("project"), expert=user)
            criteria.__dict__[field] = not criteria.__dict__[field]
            criteria.save(update_fields=[field])
            project = Project.objects.get(pk=request.GET.get("project"))
            return JsonResponse(
                {"count": project.__dict__[field], "rating": project.rating}
            )



