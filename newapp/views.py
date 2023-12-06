from django.shortcuts import render
from django.http import HttpResponse
from .models import Project




def main(request):
    project = Project.objects.all()
    return render(request, 'projects.html', {'projects': project})
