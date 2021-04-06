
from django.urls import path
from . import views
from .views import (
    PostListView,
    BlogDetailView
  
)
urlpatterns = [
    path('', views.dreamnode, name='dreamnode'),
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('social_stereotype/', views.social_stereotype, name='social_stereotype'),
 ]
