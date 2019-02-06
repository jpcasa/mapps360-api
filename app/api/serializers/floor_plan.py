from rest_framework import serializers
from ..models.floor_plan import FloorPlan

class FloorPlanSerializer(serializers.ModelSerializer):

  class Meta():
    model = FloorPlan
    fields = ('id', 'plan', 'uploaded_at')
