from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    project_url = serializers.SerializerMethodField()

    def get_project_url(self, obj):
        return f"http://localhost:8000{obj.get_absolute_url()}"

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "slug",
            "brief_description",
            "description",
            "github_repo",
            "image",
            "technologies",
            "project_date",
            "project_url",
        )
