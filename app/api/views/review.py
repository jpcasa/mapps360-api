from rest_framework import generics, permissions
from ..serializers.review import ReviewSerializer
from ..models.review import Review
from ..permissions import IsOwnerReview


class ReviewCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerReview
    )

    def get_queryset(self, *args, **kwargs):
        return Review.objects.all().filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        """Save the post data when creating a new property."""
        serializer.save(owner=self.request.user)


class ReviewDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerReview
    )
