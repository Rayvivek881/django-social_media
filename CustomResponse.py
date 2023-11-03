from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, Http404


def SuccessResponse(data, message, status_code=status.HTTP_200_OK):
  return Response({
    'success': True,
    'message': message,
    'data': data
  }, status=status_code)

def ErrorResponse(error, message, status_code=status.HTTP_400_BAD_REQUEST):
  return Response({
    'success': False,
    'message': message,
    'error': error
  }, status=status_code)