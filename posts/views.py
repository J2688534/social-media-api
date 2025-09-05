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
