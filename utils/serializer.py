from rest_framework import serializers
from .models import CloudinaryData


class CloudinaryDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = CloudinaryData
    fields = '__all__'