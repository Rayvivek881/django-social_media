from django.urls import path, include
from .views import like_toggle, PostViewSet, CommentViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('comment', CommentViewSet, basename='comments')

urlpatterns = [
  path('like/<int:pk>', like_toggle, name='like-toggle'),
  path('', include(router.urls)),
]
