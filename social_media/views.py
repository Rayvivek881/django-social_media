from rest_framework.decorators import api_view
from CustomResponse import SuccessResponse, ErrorResponse
from .models import ChatRoom, Friend, ChatObject, GroupMemberShip, Group
from .serializer import FriendSerializer, GroupSerializer
from rest_framework import viewsets, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['PATCH'])
def chatroom_add_message(request, pk):
  chatroom = ChatRoom.objects.get(id=pk)
  chatroom.add_chatobject(request.user, request.data.get('message', ''))
  return SuccessResponse(None, 'Message added to chatroom')

@api_view(['PATCH'])
def chatroom_remove_message(request, pk):
  chatroom = ChatRoom.objects.get(id=pk)
  chatroom.remove_chatobject(request.data['chatobject_id'])
  return SuccessResponse(None, 'Message removed from chatroom')

class FriendViewSet(viewsets.ViewSet):
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
  def list(self, request):
    queryset = Friend.objects.filter(members__id=request.user.id)
    serializer = FriendSerializer(queryset, many=True)
    return SuccessResponse(serializer.data, 'Friends retrieved successfully')

  def create(self, request):
    serializer = FriendSerializer(data=request.data, 
            context={'members': request.data.get('members', [])})
    serializer.is_valid(raise_exception= True)
    serializer.save()
    return SuccessResponse(serializer.data, 
       'Friend created successfully', status.HTTP_201_CREATED)

  def retrieve(self, request, pk=None):
    friend = Friend.objects.get(id=pk)
    serializer = FriendSerializer(friend)
    return SuccessResponse(serializer.data, 'Friend retrieved successfully')
 
  def destroy(self, request, pk=None):
    friend = Friend.objects.get(id=pk)
    friend.delete()
    return SuccessResponse(None, 'Friend deleted successfully')


class GroupViewSet(viewsets.ViewSet):
  def list(self, request):
    queryset = Group.objects.filter(members__id=request.user.id)
    serializer = GroupSerializer(queryset, many=True)
    return SuccessResponse(serializer.data, 'Groups retrieved successfully')

  def create(self, request):
    serializer = GroupSerializer(data=request.data, 
        context={'members': request.data.get('members', [])})
    serializer.is_valid(raise_exception= True)
    serializer.save()
    return SuccessResponse(serializer.data, 
        'Group created successfully', status.HTTP_201_CREATED)

  def retrieve(self, request, pk=None):
    group = Group.objects.get(id=pk)
    serializer = GroupSerializer(group)
    return SuccessResponse(serializer.data, 'Group retrieved successfully')
 
  def destroy(self, request, pk=None):
    group = Group.objects.get(id=pk)
    group.delete()
    return SuccessResponse(None, 'Group deleted successfully')