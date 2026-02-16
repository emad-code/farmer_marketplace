from rest_framework import permissions


class IsProductOwner(permissions.BasePermission):
    """
    Custom permission to allow only the owner of a product's farm
    to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.farm.owner == request.user