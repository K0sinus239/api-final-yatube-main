from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    PostViewSet,
    GroupViewSet,
    FollowViewSet,
)


v1_router = DefaultRouter()
v1_router.register("posts", PostViewSet, basename="posts")
v1_router.register("groups", GroupViewSet, basename="groups")
v1_router.register("follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("", include(v1_router.urls)),
]
