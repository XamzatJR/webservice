from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.users.models import CustomUser

from . import forms
from .models import Criteria, NiokrCriteria, NiokrProject, NiokrUser, Project
from .serializer import CriteriaSerializer, ProjectSerializer


class ProjectsOutputView(LoginRequiredMixin, ListView):
    """cписок всех проектов"""

    model = Project
    template_name = "projects/projects_output.html"
    context_object_name = "projects"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        kwargs["users"] = CustomUser.objects.filter()
        return super().get_context_data(**kwargs)


class UserProjectsOutputView(LoginRequiredMixin, ListView):
    """cписок своих проектов"""

    model = Project
    template_name = "projects/projects_output.html"
    context_object_name = "projects"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        kwargs["users"] = CustomUser.objects.filter()
        return super().get_context_data(**kwargs)

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
    """удаление проекта"""

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
        kwargs["users"] = CustomUser.objects.filter()

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return super().get_queryset()


# API Controllers


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["user", "responsible", "date"]
    search_fields = ["name"]


class CriteriaViewSet(ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer


class ProjectsDatesView(APIView):
    def get(self, *args, **kwargs):
        dates = {project.date for project in Project.objects.all()}
        return JsonResponse({"dates": [date.strftime("%Y-%m-%d") for date in dates]})


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


def add_responsible(request):
    if request.is_ajax():
        user = CustomUser.objects.get(pk=request.GET.get("user"))
        project = Project.objects.get(pk=request.GET.get("project"))
        responsible = (
            CustomUser.objects.get(pk=request.GET.get("responsible"))
            if request.GET.get("responsible") != "0"
            else None
        )
        if user.is_superuser:
            project.responsible = responsible
            project.save()
        return JsonResponse({"code": 200})


class NiokrProjectsOutputView(LoginRequiredMixin, ListView):
    """cписок всех НИОКР"""

    model = NiokrProject
    template_name = "projects/niokr_projects_output.html"
    context_object_name = "niokr_projects"
    paginate_by = 30

    def get_context_data(self, **kwargs):
        kwargs["users"] = CustomUser.objects.filter()
        return super().get_context_data(**kwargs)


class UserNiokrProjectsOutputView(LoginRequiredMixin, ListView):
    """cписок своих  НИОКР"""

    model = NiokrProject
    template_name = "projects/niokr_projects_output.html"
    context_object_name = "niokr_projects"
    paginate_by = 30

    def get_context_data(self, **kwargs):
        kwargs["users"] = CustomUser.objects.filter()
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return NiokrProject.objects.filter(user=self.request.user)


class NiokrProjectCreateView(LoginRequiredMixin, CreateView):
    """создание НИОКР"""

    model = NiokrProject
    template_name = "projects/niokr_project_create.html"
    form_class = forms.NiokrProjectCreateForm
    success_url = reverse_lazy("niokr_projects_list_url")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        data = super().get_form_kwargs()
        data["user"] = self.request.user
        return data


class NiokrProjectDeleteView(DeleteView, LoginRequiredMixin):
    """удаление НИОКР"""

    model = NiokrProject
    success_url = reverse_lazy("niokr_projects_list_url")
    template_name = "projects/niokr_project_delete.html"


class NiokrProjectUpdateView(LoginRequiredMixin, UpdateView):
    """редактирование НИОКР"""

    model = NiokrProject
    form_class = forms.NiokrProjectUpdateForm
    template_name = "projects/niokr_project_update.html"

    def get_success_url(self):
        return reverse_lazy("niokr_project_detail_url", kwargs={"pk": self.object.pk})

    def get_form_kwargs(self):
        data = super().get_form_kwargs()
        data["user"] = self.request.user
        return data


class NiokrProjectDetailView(LoginRequiredMixin, DetailView):
    """обзор НИОКР"""

    model = NiokrProject
    template_name = "projects/niokr_project_detail.html"
    success_url = reverse_lazy("niokr_project_detail_url")
    context_object_name = "niokr_projects"

    def get_context_data(self, **kwargs):
        if self.request.user.is_expert:
            niokr_criteria = NiokrCriteria.objects.get_or_create(
                app=kwargs["object"], expert=self.request.user
            )
        try:
            kwargs["niokr_criteria"] = niokr_criteria[0]
        except UnboundLocalError:
            forms.NiokrCriteriaForm
        kwargs["users"] = CustomUser.objects.filter()

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return super().get_queryset()


def change_niokr_criteria(request):
    if request.is_ajax():
        field = request.GET.get("field")
        user = CustomUser.objects.get(pk=request.GET.get("user"))
        if user.is_expert:
            niokr_criteria = NiokrCriteria.objects.get(
                app=request.GET.get("niokr_projects"), expert=user
            )
            niokr_criteria.__dict__[field] = not niokr_criteria.__dict__[field]
            niokr_criteria.save(update_fields=[field])
            niokr_project = NiokrProject.objects.get(
                pk=request.GET.get("niokr_projects")
            )
            return JsonResponse(
                {"count": niokr_project.__dict__[field], "rating": niokr_project.rating}
            )


class NiokrProjectsDatesView(APIView):
    def get(self, *args, **kwargs):
        dates = {niokr_project.date for niokr_project in NiokrProject.objects.all()}
        return JsonResponse({"dates": [date.strftime("%Y-%m-%d") for date in dates]})


class NiokrUserCreateView(LoginRequiredMixin, CreateView):
    """создание научного руководителя"""

    model = NiokrUser
    template_name = "projects/niokr_user_create.html"
    form_class = forms.NiokrUserCreate
    success_url = reverse_lazy("niokr_user_create_url")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
