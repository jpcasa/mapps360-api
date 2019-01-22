from rest_framework.permissions import BasePermission
from .models.property import Property


class IsOwner(BasePermission):
    """Custom permission class to allow only property owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the property owner."""
        if isinstance(obj, Property):
            return obj.owner == request.user
        return obj.owner == request.user
