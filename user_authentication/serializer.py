from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserDetails

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class UserDetailsSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only = True)
  class Meta:
    model = UserDetails
    fields = '__all__'