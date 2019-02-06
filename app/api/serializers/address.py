from rest_framework import serializers
from ..models.address import City, Country, Address


class CitySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = City
        fields = (
            'id',
            'name',
            'code',
            'date_created',
            'date_modified'
        )
        read_only_fields = ('date_created', 'date_modified')


class CountrySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Country
        fields = (
            'id',
            'cities',
            'name',
            'code',
            'date_created',
            'date_modified'
        )
        read_only_fields = ('date_created', 'date_modified')


class AddressSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Address
        fields = (
            'id',
            'owner',
            'name',
            'additional',
            'postal_code',
            'lat',
            'long',
            'city',
            'country',
            'date_created',
            'date_modified'
        )
        read_only_fields = ('date_created', 'date_modified')
