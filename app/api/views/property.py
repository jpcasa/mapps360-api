from rest_framework import generics, permissions
from ..serializers.property import PropertySerializer
from ..models.property import Property
from ..permissions import IsOwner


class PropertyCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner
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
        IsOwner
    )
