from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class EventList(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:event_list_detail', args=[self.slug])
    
class Post(models.Model):
    image_post = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    event_list = models.ForeignKey(EventList, on_delete=models.CASCADE, related_name='posts')  # Associate posts with an event list

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[self.slug])

