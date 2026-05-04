from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Доступ на чтение для всех, редактирование и удаление только для автора.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if hasattr(obj, "author"):
            return obj.author == request.user
        return False
