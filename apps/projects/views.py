from rest_framework.viewsets import ModelViewSet

from .models import Project
from .serializer import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
