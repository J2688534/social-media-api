from rest_framework import serializers
from .models import Post, Comment, Like


from rest_framework import serializers
from .models import Post, Comment, Like


from rest_framework import serializers
from .models import Post, Comment, Like


# Comment Serializer (without post)
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "content", "created_at"]  # removed "post"
        read_only_fields = ["id", "user", "created_at"]



# Like Serializer (without post)

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ["id", "user", "created_at"]  # removed "post"
        read_only_fields = ["id", "user", "created_at"]


# Post Serializer (with nested comments + likes)
class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "content",
            "created_at",
            "likes_count",
            "comments_count",
            "comments",
            "likes",
        ]
        read_only_fields = ["id", "user", "created_at"]

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()
