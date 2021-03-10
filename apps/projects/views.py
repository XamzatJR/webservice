from rest_framework import generics
from rest_framework.response import Response

from .models import Project
from .serializer import ProjectSerializer


class ProjectView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer