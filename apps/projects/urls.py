from .views import ProjectViewSet, CriteriaViewSet
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"criteria", CriteriaViewSet)

urlpatterns = [
    path("", views.index, name="index_url"),
]
