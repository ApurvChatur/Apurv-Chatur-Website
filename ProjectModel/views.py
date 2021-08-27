from django.shortcuts import render, get_object_or_404, get_list_or_404
from ProjectDesign.models import (Home,
                                  About,
                                  Intrest,
                                  Project,
                                  )


def home_view(request):
    home = get_object_or_404(Home, title='Apurv Chatur')

    template_name = 'ProjectModel/a-home-page.html'
    context = {
        'title': 'Home',
        'home': home,
    }
    return render(request, template_name, context)


def about_view(request):
    about = get_object_or_404(About, title='About Me')

    template_name = 'ProjectModel/b-about-page.html'
    context = {
        'title': 'About',
        'about': about,
    }
    return render(request, template_name, context)


def intrests_view(request):
    intrests = get_list_or_404(Intrest)

    template_name = 'ProjectModel/c-intrests-page.html'
    context = {
        'title': 'Intrests',
        'intrests': intrests,
    }
    return render(request, template_name, context)


def projects_view(request):
    projects = get_list_or_404(Project)

    template_name = 'ProjectModel/d-projects-page.html'
    context = {
        'title': 'Projects',
        'projects': projects,
    }
    return render(request, template_name, context)


def project_view(request, slug):
    project = get_object_or_404(Project, slug=slug)

    template_name = 'ProjectModel/e-project-page.html'
    context = {
        'title': f'Project - {project.title}',
        'project': project,
    }
    return render(request, template_name, context)


def contact_view(request):

    template_name = 'ProjectModel/f-contact-page.html'
    context = {
        'title': 'Contact',
    }
    return render(request, template_name, context)
