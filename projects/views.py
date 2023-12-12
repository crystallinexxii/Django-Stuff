from django.shortcuts import render
from django.http import HttpResponse
from .models import Project




def main(request):
    project = Project.objects.all()
    return render(request, 'projects.html', {'projects': project})


def project_details(request, project_id):
    project = Project.objects.get(slug=project_id)
    return render(request, 'project-details.html', {'project': project})
