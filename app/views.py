from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from app.models import Project


def index(request):
    projects = Project.objects.all()
    themes = []
    for c in Project.objects.all():
        themes.append(c.theme)
    themes.sort()
    return render(request, 'home.html', context={"projects": projects, 'themes': themes})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project.html', context={"project": project})
