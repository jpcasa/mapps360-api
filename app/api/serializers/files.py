from rest_framework import serializers
from ..models.files import File

class FileSerializer(serializers.ModelSerializer):

  class Meta():
    model = File
    fields = ('file', 'remark', 'timestamp')
