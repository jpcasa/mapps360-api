from rest_framework import serializers
from ..models.review import Review

class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta():
        model = Review
        fields = (
            'id',
            'owner',
            'stars',
            'review', 
            'uploaded_at'
        )
