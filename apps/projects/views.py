from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Project
from .serializer import ProjectSerializer


class ProjectView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response({"projects": serializer.data})

    def post(self, request):
        project = request.data.get("project")
        serializer = ProjectSerializer(data=project)
        if serializer.is_valid(raise_exception=True):
            project_saved = serializer.save()
        return Response(
            {"success": "Project '{}' created successfully".format(projcet_saved.title)}
        )

    def put(self, request, pk):
        saved_project = get_object_or_404(Project.objects.all(), pk=pk)
        data = request.data.get("project")
        serializer = ProjectSerializer(instance=saved_project, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            project_saved = serializer.save()

        return Response(
            {"success": "Project '{}' updated successfully".format(project_saved.title)}
        )

    def delete(self, request, pk):
        project = get_object_or_404(Project.objects.all(), pk=pk)
        project.delete()
        return Response(
            {"message": "Project with id `{}` has been deleted.".format(pk)}, status=204
        )
