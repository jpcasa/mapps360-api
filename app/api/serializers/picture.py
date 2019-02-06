from rest_framework import serializers
from ..models.picture import Picture

class PictureSerializer(serializers.ModelSerializer):

  class Meta():
    model = Picture
    fields = ('id', 'image', 'show', 'uploaded_at')
