from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializer import Project, ProjectSerializer


class ProjectCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny,)
