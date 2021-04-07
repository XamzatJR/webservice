from django.conf.urls import include
from django.urls import path
from django.urls.conf import re_path
from rest_framework.routers import DefaultRouter

from . import views
from .views import CriteriaViewSet, ProjectViewSet, change_criteria, ProjectDeleteView, ProjectUpdateView

router = DefaultRouter()
router.register(r"api/projects", ProjectViewSet)
router.register(r"criteria", CriteriaViewSet)

urlpatterns = [
    path("", views.ProjectsOutputView.as_view(), name="index_url"),
    path("projects/", views.ProjectsOutputView.as_view(), name="projects_list_url"),
    path(
        "projects/<int:pk>/",
        views.ProjectDetailView.as_view(),
        name="project_detail_url",
    ),
    path(
        "project_delete/<int:pk>/",
        views.ProjectDeleteView.as_view(),
        name="project_delete_url",
    ),
    path(
        "project_update/<int:pk>",
        views.ProjectUpdateView.as_view(),
        name="project_update_url",
    ),
    path(
        "projects/create/", views.ProjectCreateView.as_view(), name="project_create_url"
    ),
    path(
        "my_projects/",
        views.UserProjectsOutputView.as_view(),
        name="user_projects_list_url",
    ),
    path(
        "project/<int:pk>/",
        views.ProjectsOutputView.as_view(),
        name="project_output_pk_url",
    ),
    path(
        "project_responsible/<int:pk>",
        views.ProjectAddResponsible.as_view(),
        name="project_add_responsible_url",
    ),
    path("change_criteria/", change_criteria, name="change_criteria"),
    re_path("^", include(router.urls)),
]
