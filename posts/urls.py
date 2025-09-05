from django.urls import path
from .views import CommentListCreateView, CommentDetailView

urlpatterns = [
    # Comments for a specific post
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
