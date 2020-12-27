from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('post/<int:pk>/',  PostDetailView.as_view(), name='detail_post'),
    path('post/new/',  PostCreateView.as_view(), name='new_post'),
    path('post/update/<int:pk>/',  PostUpdateView.as_view(), name='update_post'),
    path('post/delete/<int:pk>/',  PostDeleteView.as_view(), name='delete_post'),
]
