from rest_framework import permissions


# class AccessToOwnTasks(permissions.BasePermission):
#     """Allow users to get, create, edit and delete their own tasks"""

#     def has_object_permission(self, request, view, obj):
#         """Check user is trying to edit their own profile"""
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         return obj.user.id == request.user.id
