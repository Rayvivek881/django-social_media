from django.shortcuts import render
from rest_framework import viewsets

from CustomResponse import SuccessResponse
from utils.serializer import CloudinaryDataSerializer
from .models import CloudinaryData
from rest_framework.decorators import api_view
import cloudinary

# Create your views here.

@api_view(['POST'])
def upload_by_singles(request):
  Arr = []
  for key, value in request.FILES.items():
    obj = cloudinary.uploader.upload(value)
    result = CloudinaryDataSerializer(data={'link': obj['url'],
              'name': key, 'type': obj['resource_type']})
    result.is_valid(raise_exception=True)
    result.save()
    Arr.append(result)
  return SuccessResponse(Arr, "Cloudinary data created successfully")


@api_view(['POST'])
def upload_by_Arr(request):
  lst = []
  for _, Arr in request.FILES.items():
    for value in Arr:
      obj = cloudinary.uploader.upload(value)
      lst.append(CloudinaryData.objects.create(link=obj['url'], 
                    name=obj['public_id'], type=obj['resource_type']))
  return lst
      