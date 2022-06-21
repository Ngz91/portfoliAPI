from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

import rest_framework.permissions as permissions

from .models import Project
from .serializers import ProjectSerializer


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def ApiOverview(request):
    api_urls = {
        "Projects": "api/projects",
        "Project Details": "api/project/<id>/<slug>",
    }

    return Response(api_urls)


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def ProjectsList(request):
    projects = Project.objects.all().order_by("-id")
    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def ProjectDetails(request, id, slug):
    project = Project.objects.get(id=id, slug=slug)
    serializer = ProjectSerializer(project, many=False)

    return Response(serializer.data)
