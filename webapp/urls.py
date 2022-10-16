from django.urls import path

from webapp.views import LProjectView, DetailProjectView, about, search #

app_name = 'webapp'

urlpatterns = [
    path('', LProjectView.as_view(), name='home'),
    path('project/<int:pk>/', DetailProjectView.as_view(), name='project_detail'),
    path('about/', about, name='about'),
    path('search/', search, name='search_results')
]