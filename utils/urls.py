from django.urls import path, include
from rest_framework import routers

from .views import upload_by_Arr, upload_by_singles

router = routers.DefaultRouter()

urlpatterns = [
  path('upload/singles/', upload_by_singles, name = "singles"),
  path('upload/Arr/', upload_by_Arr, name = "Arr"),
  path('', include(router.urls)),
]
