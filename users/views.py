from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model() 
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UserSerializer, FollowSerializer
from .models import Follow


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class FollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        follower = request.user
        try:
            following = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        if follower == following:
            return Response({"error": "You cannot follow yourself"}, status=400)

        follow, created = Follow.objects.get_or_create(follower=follower, following=following)
        if not created:
            return Response({"detail": "Already following"}, status=400)

        return Response(FollowSerializer(follow).data, status=201)

    def delete(self, request, user_id):
        follower = request.user
        try:
            following = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        follow = Follow.objects.filter(follower=follower, following=following).first()
        if not follow:
            return Response({"detail": "Not following"}, status=400)

        follow.delete()
        return Response({"detail": "Unfollowed successfully"}, status=204)
