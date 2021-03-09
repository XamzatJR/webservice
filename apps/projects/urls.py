from .views import ProjectView
from django.urls import path


urlpatterns = [
    path("projects/", ProjectView.as_view()),
    path("projects/<int:pk>", ProjectView.as_view()),
]
