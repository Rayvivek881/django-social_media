from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer, UserDetailsSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDetailsViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserDetailsSerializer