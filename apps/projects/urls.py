from .views import ProjectViewSet, ProjectCriteriaView
from django.urls import re_path, include, path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("projects", ProjectViewSet)

urlpatterns = [
    re_path("^", include(router.urls)),
    path("criteria/<int:pk>", ProjectCriteriaView.as_view()),
]
