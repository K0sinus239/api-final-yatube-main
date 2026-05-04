from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from api.views import (
    PostViewSet,
    GroupViewSet,
    FollowViewSet,
    CommentViewSet,
)

v1_router = DefaultRouter()
v1_router.register("posts", PostViewSet, basename="posts")
v1_router.register("groups", GroupViewSet, basename="groups")
v1_router.register("follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("", include(v1_router.urls)),
    re_path(
        r"^posts/(?P<post_id>\d+)/comments/$",
        CommentViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="post-comments-list",
    ),
    re_path(
        r"^posts/(?P<post_id>\d+)/comments/(?P<pk>\d+)/$",
        CommentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="post-comment-detail",
    ),
]