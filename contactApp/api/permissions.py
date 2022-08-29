from rest_framework import permissions
from rest_framework import serializers


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            raise serializers.ValidationError({'error': 'This method cannot be accessed!'})

