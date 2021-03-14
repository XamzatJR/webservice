from rest_framework.viewsets import ModelViewSet

from rest_framework.generics import UpdateAPIView

from django_filters.rest_framework import DjangoFilterBackend

from .models import Project, Criteria
from .serializer import ProjectSerializer, CriteriaSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "name", "responsible"]


class ProjectCriteriaView(UpdateAPIView):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer
