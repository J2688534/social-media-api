from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, FollowView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/<int:pk>/", UserDetailView.as_view(), name="user-profile"),
    path("follow/<int:user_id>/", FollowView.as_view(), name="follow-unfollow"),
]
