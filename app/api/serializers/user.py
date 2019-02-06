from rest_framework import serializers
from . import Property
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    properties = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Property.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'groups',
            'user_permissions',
            'is_staff',
            'is_active',
            'is_superuser',
            'last_login',
            'date_joined',
            'properties'
        )
