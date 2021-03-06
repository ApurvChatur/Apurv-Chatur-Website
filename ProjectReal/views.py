from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.mail import send_mail
from ProjectDesign.models import (Home,
                                  About,
                                  Intrest,
                                  Project,
                                  )


def home_view(request):
    home = get_object_or_404(Home, title='Apurv Chatur')
    about = get_object_or_404(About, title='About Me')
    intrests = get_list_or_404(Intrest)
    projects = get_list_or_404(Project)

    if request.method == "POST":
        send_mail(
            subject='Thanks Dude',
            message='hahaha',
            from_email='chaturapurv@gmail.com',
            recipient_list=['chaturapurv@gmail.com']
        )

    template_name = 'ProjectReal/home-page.html'
    context = {
        'home': home,
        'about': about,
        'intrests': intrests,
        'projects': projects,
    }
    return render(request, template_name, context)


def project_view(request, slug):
    project = get_object_or_404(Project, slug=slug)

    template_name = 'ProjectReal/project-page.html'
    context = {
        'project': project,
    }
    return render(request, template_name, context)

