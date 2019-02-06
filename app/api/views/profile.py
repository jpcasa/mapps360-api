from rest_framework import generics, permissions
from ..serializers.profile import ProfileSerializer
from ..models.profile import Profile
from ..permissions import IsOwnerProfile


class ProfileListView(generics.ListAPIView):
    """This class defines the list behavior of our rest api."""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    )

    def get_queryset(self, *args, **kwargs):
        return Profile.objects.all().filter(
            user=self.request.user
        )


class ProfileCreateView(generics.CreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        """Save the post data when creating a new profile."""
        serializer.save(user=self.request.user)


class ProfileDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerProfile
    )
