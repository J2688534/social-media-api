from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture", "password"]

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            bio=validated_data.get("bio", ""),
            profile_picture=validated_data.get("profile_picture", ""),
        )
        user.set_password(validated_data["password"])  
        user.save()
        return user
