from django.urls import path
from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    LikeView,
    DisLikeView,
    BlogCreateView,
    EventListView,
    EventListDetailView,
)

# from .views import BlogListView, BlogDetailView, LikeView, DisLikeView, BlogCreateView

app_name = 'blog'

# urlpatterns = [
#     path('', BlogListView.as_view(), name='blog_list'),
#     path('create/', BlogCreateView.as_view(), name='blog_create'),  # Place this before <slug:slug>
#     path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
#     path('like_post/<int:pk>', LikeView, name='like_post'),
#     path('dislike_post/<int:pk>', DisLikeView, name='dislike_post'),
# ]

 

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<slug:slug>/', EventListDetailView.as_view(), name='event_list_detail'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('like_post/<int:pk>', LikeView, name='like_post'),
    path('dislike_post/<int:pk>', DisLikeView, name='dislike_post'),
]
