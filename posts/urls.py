from django.urls import path
from .views import CommentListCreateView, CommentDetailView

urlpatterns = [
    # Comments for a specific post
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
from .views import LikePostView

urlpatterns += [
    path('posts/<int:post_id>/like/', LikePostView.as_view(), name='like-post'),
]

from .views import FeedView

urlpatterns += [
    path('feed/', FeedView.as_view(), name='feed'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Social Media API"})
