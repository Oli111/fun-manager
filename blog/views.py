from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail

def LikeView(request, pk):
    selected_post = get_object_or_404(Post, id =request.POST.get('post_id'))
    selected_post.votes = 1
    selected_post.save()
    return HttpResponseRedirect(reverse('blog:blog_list'))

def DisLikeView(request, pk):
    selected_post = get_object_or_404(Post, id =request.POST.get('post_id_no'))
    selected_post.votes = -1
    selected_post.save()
    return HttpResponseRedirect(reverse('blog:blog_list'))

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'
