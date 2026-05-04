from rest_framework import serializers

from posts.models import Comment, Post, Group, Follow

from django.contrib.auth import get_user_model

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Comment
        read_only_fields = ("author", "post")


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
    )
    following = serializers.SlugRelatedField(   # ← добавь поле
        slug_field="username",
        queryset=User.objects.all(),
    )

    class Meta:
        fields = ("user", "following")
        model = Follow
