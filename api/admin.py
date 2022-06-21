from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "description", "project_date")
    list_filter = ("slug", "project_date")
    list_editable = ("description", "project_date")
    prepopulated_fields = {"slug": ("name",)}
