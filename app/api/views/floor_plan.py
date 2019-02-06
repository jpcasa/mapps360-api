from rest_framework import generics, permissions
from ..serializers.floor_plan import FloorPlanSerializer
from ..models.floor_plan import FloorPlan
from ..permissions import IsOwnerFloorPlan


class FloorPlanCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = FloorPlan.objects.all()
    serializer_class = FloorPlanSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerFloorPlan
    )

    def get_queryset(self, *args, **kwargs):
        return FloorPlan.objects.all().filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        """Save the post data when creating a new property."""
        serializer.save(owner=self.request.user)


class FloorPlanDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = FloorPlan.objects.all()
    serializer_class = FloorPlanSerializer

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerFloorPlan
    )
