from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from webapp.models import Project


class LProjectView(ListView):
    model = Project
    template_name = 'webapp/project_list.html'
    queryset = Project.objects.all()
    context_object_name = 'projects'



class DetailProjectView(DetailView):
    model = Project
    template_name = 'webapp/project_detail.html'


def about(request):
    return render(request, 'webapp/about.html')


def search(request):
    text = request.GET.get('search')
    if text:
        projects = Project.objects.filter(
            Q(title__contains=text)|Q(description__contains=text)
        )
    else:
        projects = Project.objects.none()
    return render(request, 'webapp/search_results.html', {'projects': projects})
