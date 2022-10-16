from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from blog.models import Post, Category, Comment
from blog.form import CommentForm



class LBlogView(ListView):
    model = Post
    template_name = 'blog/blog_index.html'
    # queryset = Post.objects.all().order_by('-created_at')
    def get_queryset(self):
        posts = Post.objects.all().order_by('-created_at').filter(pk__in=[1,3])
        return posts



class DetailBlogView(FormMixin, DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    form_class = CommentForm


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=self.object
            )
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super(DetailBlogView, self).get_context_data(**kwargs)
        post = self.get_object()
        comments = Comment.objects.filter(post=post).order_by('-created_at')
        context['post'] = post
        context['comments'] = comments
        return context


    def get_success_url(self):
        print()
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.id})



def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('created_at')
    context = {'posts': posts, 'category': category}
    return render(request, 'blog/blog_category.html', context=context)
