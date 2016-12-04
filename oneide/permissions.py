from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # for GET, OPTIONS or HEAD
        if request.method in permissions.SAFE_METHODS:
            return True
        # for POST, PUT, DELETE
        return obj.owner == request.user