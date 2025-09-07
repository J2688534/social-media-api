from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer

# List + Create comments for a post
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(user=self.request.user, post_id=post_id)


# Retrieve, Update, Delete a specific comment
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.user:
            raise PermissionError("You can only edit your own comments.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.user:
            raise PermissionError("You can only delete your own comments.")
        instance.delete()

from .models import Like
from .serializers import LikeSerializer
from rest_framework.response import Response
from rest_framework import status

# Like / Unlike a post
class LikePostView(generics.GenericAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        user = request.user
        existing_like = Like.objects.filter(user=user, post_id=post_id).first()

        if existing_like:
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like = Like.objects.create(user=user, post_id=post_id)
        return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)

    def delete(self, request, post_id):
        user = request.user
        like = Like.objects.filter(user=user, post_id=post_id).first()

        if not like:
            return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"detail": "Unliked successfully."}, status=status.HTTP_204_NO_CONTENT)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from .models import Post
from .serializers import PostSerializer


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Add filters, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['timestamp']   # filter by exact date/time
    search_fields = ['content']        # search by keyword in post content
    ordering_fields = ['timestamp']    # order by newest/oldest

    def get_queryset(self):
        user = self.request.user
        # Only return posts from users the current user follows
        following_users = user.following.values_list('following_id', flat=True)
        return Post.objects.filter(author__id__in=following_users).order_by('-timestamp')

from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Social Media API!"})
