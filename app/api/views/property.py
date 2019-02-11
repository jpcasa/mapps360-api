from django.db.models import Q
from rest_framework import generics, permissions
from ..serializers.property import (
    PropertySerializer, PropertyListSerializer)
from ..models.property import Property, PropertyList
from ..permissions import IsOwnerProperty, IsOwnerPropertyList


class PropertyCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    serializer_class = PropertySerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerProperty
    )

    def get_queryset(self, *args, **kwargs):
        return Property.objects.all().filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        """Save the post data when creating a new property."""
        serializer.save(owner=self.request.user)


class PropertyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerProperty
    )


class PropertyListListView(generics.ListAPIView):
    """This class defines the list behavior of our rest api."""
    serializer_class = PropertyListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self, *args, **kwargs):
        return PropertyList.objects.filter(
            Q(owner=self.request.user) |
            Q(participants__user=self.request.user)
        ).distinct()


class PropertyListCreateView(generics.CreateAPIView):
    """This class defines the list behavior of our rest api."""
    serializer_class = PropertyListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        """Save the post data when creating a new property."""
        serializer.save(owner=self.request.user)


class PropertyListDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = PropertyList.objects.all()
    serializer_class = PropertyListSerializer

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerPropertyList
    )
