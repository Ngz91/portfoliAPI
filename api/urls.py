from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.ApiOverview, name='api-overview'),
    path('projects/', views.ProjectsList, name='projects-list'),
    path('project/<int:id>/<slug:slug>/', views.ProjectDetails, name="project-details"),
]
