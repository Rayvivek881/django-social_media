
from django.urls import path, include
from .views import chatroom_add_message, chatroom_remove_message, FriendViewSet, GroupViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('friends', FriendViewSet, basename='friends')
router.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
  path('chatroom/<int:pk>/add_message/', chatroom_add_message, name='chatroom-add-message'),
  path('chatroom/<int:pk>/remove_message/', chatroom_remove_message, name='chatroom-remove-message'),
  path('', include(router.urls)),
]