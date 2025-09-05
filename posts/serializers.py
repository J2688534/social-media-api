from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # show username instead of ID

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
