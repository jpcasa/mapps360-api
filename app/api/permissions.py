from rest_framework.permissions import BasePermission

from .models.address import City, Country, Address
from .models.floor_plan import FloorPlan
from .models.picture import Picture
from .models.profile import Profile
from .models.property import Property
from .models.review import Review


class IsOwnerAddress(BasePermission):
    """Custom permission class to allow only address owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the address owner."""
        if isinstance(obj, Address):
            return obj.owner == request.user
        return obj.owner == request.user


class IsOwnerFloorPlan(BasePermission):
    """Custom permission class to allow only floor plan owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the floor plan owner."""
        if isinstance(obj, FloorPlan):
            return obj.owner == request.user
        return obj.owner == request.user


class IsOwnerPicture(BasePermission):
    """Custom permission class to allow only picture owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the picture owner."""
        if isinstance(obj, Picture):
            return obj.owner == request.user
        return obj.owner == request.user


class IsOwnerProfile(BasePermission):
    """Custom permission class to allow only profile owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the profile owner."""
        if isinstance(obj, Profile):
            return obj.user == request.user
        return obj.user == request.user


class IsOwnerProperty(BasePermission):
    """Custom permission class to allow only property owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the property owner."""
        if isinstance(obj, Property):
            return obj.owner == request.user
        return obj.owner == request.user


class IsOwnerReview(BasePermission):
    """Custom permission class to allow only picture owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the picture owner."""
        if isinstance(obj, Review):
            return obj.owner == request.user
        return obj.owner == request.user
