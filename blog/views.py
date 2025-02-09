from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail

def LikeView(request, pk):
    selected_post = get_object_or_404(Post, id =request.POST.get('post_id')) # Get id of the pos
    selected_post.votes = 1 # increase votes for post_id
    selected_post.save() # save votes for post_id
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

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post, EventList

class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'body', 'slug', 'author']  # Specify fields for the form
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')  # Redirect after successful creation

class EventListView(ListView):
    model = EventList
    context_object_name = 'event_lists'
    template_name = 'blog/event_list.html'

class EventListDetailView(DetailView):
    model = EventList
    context_object_name = 'event_list'
    template_name = 'blog/event_list_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.all()  # Get posts related to this event list
        return context