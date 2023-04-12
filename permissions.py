from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = 'permissiondenide, you are not the owner'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user