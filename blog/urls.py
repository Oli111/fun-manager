from django.urls import path
from .views import BlogListView, BlogDetailView, LikeView, DisLikeView

app_name = 'blog'

urlpatterns = [
    # post views
    path('', BlogListView.as_view(), name='blog_list'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('like_post/<int:pk>', LikeView, name = 'like_post'),
    path('dislike_post/<int:pk>', DisLikeView, name = 'dislike_post'),
]
