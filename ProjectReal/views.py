from django.shortcuts import render, get_object_or_404, get_list_or_404


def home_view(request):
    template_name = 'ProjectReal/home-page.html'
    context = {}
    return render(request, template_name, context)

