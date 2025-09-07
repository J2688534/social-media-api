from django.urls import path
from .views import CommentListCreateView, CommentDetailView



from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Social Media API"})
from django.urls import path
from .views import (
    PostListCreateView, PostDetailView, FeedView,
    CommentListCreateView, CommentDetailView,
    LikePostView
)
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Social Media API"})

urlpatterns = [
    # Home
    path('', home, name='home'),

    # Posts
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/feed/", FeedView.as_view(), name="feed"),

    # Comments
    path("posts/<int:post_id>/comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("posts/comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),

    # Likes
    path("posts/<int:post_id>/like/", LikePostView.as_view(), name="like-post"),
]