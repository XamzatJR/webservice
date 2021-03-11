from .views import ProjectViewSet
from django.urls import re_path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("projects", ProjectViewSet)

urlpatterns = [
    re_path("^", include(router.urls)),
]
