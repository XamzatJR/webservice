from .views import ProjectViewSet, CriteriaViewSet, change_criteria
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
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
]
