from django.shortcuts import render, get_object_or_404, get_list_or_404
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

    template_name = 'ProjectReal/home-page.html'
    context = {
        'home': home,
        'about': about,
        'intrests': intrests,
        'projects': projects,
    }
    return render(request, template_name, context)

