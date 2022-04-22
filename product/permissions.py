from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated and request.user.is_staff

    def has_object_permission(self, request, obj, view):
        print(SAFE_METHODS)
        print(request.user)
        print(request.user.is_authenticated)
        print(request.user.is_staff)
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)


# class IsAuthorOrReadonly(permissions.BasePermission):
#     """
#     Create  permission to only allow owner of an object to edit and delete it.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         return obj.author == request.user
#
#
# class IsUserOrReadOnly(permissions.BasePermission):
#     """
#     Create permissions to only allow owner of an object to edit and delete it
#     """
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.user == request.user
#
