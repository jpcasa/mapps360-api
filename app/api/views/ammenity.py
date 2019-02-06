from rest_framework import generics, permissions
from ..serializers.ammenity import AmmenitySerializer
from ..models.ammenity import Ammenity


class AmmenityCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Ammenity.objects.all()
    serializer_class = AmmenitySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        """Save the post data when creating a new property."""
        serializer.save(owner=self.request.user)


class AmmenityDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Ammenity.objects.all()
    serializer_class = AmmenitySerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )
