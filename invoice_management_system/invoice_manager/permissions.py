from rest_framework.permissions import BasePermission , SAFE_METHODS

from django.conf import settings


class RolePermission(BasePermission):

    # def has_permission(self, request, view):
    #     if request.user and request.user.is_staff :
    #         return True
    #     if request.method in SAFE_METHODS and request.user.is_authenticated and not request.user.is_staff:
    #         return True
    #     return False


    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff or request.user.is_superuser:
            return True
        if request.method in SAFE_METHODS and request.user.is_authenticated and not request.user.is_staff:
            return True
        return False
