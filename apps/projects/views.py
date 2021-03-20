from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project, Criteria
from .serializer import ProjectSerializer, CriteriaSerializer
from django.shortcuts import render


def index(request):
    return render(request, "projects/index.html")


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "name", "responsible"]


class CriteriaViewSet(ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer
