from rest_framework import serializers
from ..models.property import Property


class PropertySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Property
        fields = (
            'id',
            'owner',
            'name',
            'url',
            'address',
            'ammenities',
            'description',
            'price',
            'mode',
            'type',
            'year_built',
            'square_meters',
            'rooms',
            'bathrooms',
            'garages',
            'pictures',
            'floor_plan',
            'status',
            'date_created',
            'date_modified'
        )
        read_only_fields = ('date_created', 'date_modified')
