from .views import ProjectDetail, ProjectView
from django.urls import path


urlpatterns = [
    path("projects/", ProjectView.as_view()),
    path("projects/<int:pk>/", ProjectDetail.as_view()),
]
