from rest_framework import generics, permissions
from ..serializers.picture import PictureSerializer
from ..models.picture import Picture
from ..permissions import IsOwnerPicture


class PictureCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerPicture
    )

    def get_queryset(self, *args, **kwargs):
        return Picture.objects.all().filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        """Save the post data when creating a new property."""
        serializer.save(owner=self.request.user)


class PictureDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerPicture
    )
