from django.urls import path
from .views import (home_view,
                    about_view,
                    intrests_view,
                    projects_view,
                    project_view,
                    contact_view,
                    )

app_name = 'ProjectModel'

urlpatterns = [
    path('', home_view, name='home-page'),
    path('about/', about_view, name='about-page'),
    path('intrests/', intrests_view, name='intrests-page'),
    path('projects/', projects_view, name='projects-page'),
    path('project/<slug>/', project_view, name='project-page'),
    path('contact/', contact_view, name='contact-page'),
]
