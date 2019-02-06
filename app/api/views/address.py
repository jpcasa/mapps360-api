from rest_framework import generics, permissions
from ..serializers.address import (
    CitySerializer, CountrySerializer, AddressSerializer)
from ..models.address import City, Country, Address
from ..permissions import IsOwnerAddress


class CityCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self, *args, **kwargs):
        return City.objects.all().filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        """Save the post data when creating a new property."""
        serializer.save(owner=self.request.user)


class CityDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = City.objects.all()
    serializer_class = CitySerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )


class CountryCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self, *args, **kwargs):
        return Country.objects.all().filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        """Save the post data when creating a new property."""
        serializer.save(owner=self.request.user)


class CountryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )


class AddressCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerAddress
    )

    def get_queryset(self, *args, **kwargs):
        return Address.objects.all().filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        """Save the post data when creating a new property."""
        serializer.save(owner=self.request.user)


class AddressDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerAddress
    )
