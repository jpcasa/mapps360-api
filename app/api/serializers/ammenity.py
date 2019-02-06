from rest_framework import serializers
from ..models.ammenity import Ammenity

class AmmenitySerializer(serializers.ModelSerializer):

  class Meta():
    model = Ammenity
    fields = ('id', 'owner', 'name', 'icon', 'uploaded_at')
