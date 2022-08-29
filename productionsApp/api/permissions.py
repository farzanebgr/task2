from rest_framework import permissions
from rest_framework import serializers


# Permission for admin or read data
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        admin = bool(request.user and request.user.is_staff)
        if admin or (request.method in permissions.SAFE_METHODS):
            return True
        else:
            raise serializers.ValidationError({'error': 'This method cannot be accessed!'})


# Permission for admin or read data
class IsAdminOrIsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        admin = bool(request.user or request.user.is_staff)
        if admin or (request.method in permissions.SAFE_METHODS):
            return True
        else:
            raise serializers.ValidationError({'error': 'This method cannot be accessed!'})
