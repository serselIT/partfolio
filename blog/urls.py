from django.urls import path

from blog.views import LBlogView, DetailBlogView, blog_category #blog_index, blog_detail,

app_name = 'blog'

urlpatterns = [
    path('', LBlogView.as_view(), name='blog_index'),
    path('<int:pk>/', DetailBlogView.as_view(), name='blog_detail'),
    path('<category>/', blog_category, name='blog_category'),
]