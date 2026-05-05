from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, CommentViewSet

v1_router = DefaultRouter()
v1_router.register("posts", PostViewSet, basename="posts")
v1_router.register("comments", CommentViewSet, basename="comments")                                                            

urlpatterns = [
    path("", include(v1_router.urls)),
]
