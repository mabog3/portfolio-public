from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Project, Club
# Create your views here.
import logging


navitems = [("Home", '/home/'), ("Projects", '/projects/'), ("Experience", '/experience/'), ("Campus", '/campus/'),] #("Interests", '/interests/')]

def projects(request): 
    projects = Project.objects
    return render(request, 'jobs/home.html', {'projects_list':projects, 'navitems':navitems}) #returns an html file; has to exist in a folder jobs/templates/jobs

def clubs(request):
    clubs = Club.objects
    return render(request, 'jobs/clubs.html', {'jobs_list':clubs, 'navitems':navitems})

def homepg(request):
    return render(request, 'mainTemp.html', {'navitems':navitems})

def jobs(request):
    jobs = Job.objects
    return render(request, 'jobs/jobs.html', {'jobs_list':jobs, 'navitems':navitems})

def detail(request, proj_id):
    proj_detail = get_object_or_404(Project, pk=proj_id) #returns a project detail
    return render(request, 'jobs/projDetail.html', {'proj':proj_detail, 'navitems':navitems})

def redirect_view(request):
    response = redirect('home')
    return response