from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ChatObject, ChatRoom, Friend, GroupMemberShip, Group

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username']

class ChatObjectSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)
  class Meta:
    model = ChatObject
    fields = '__all__'

class ChatRoomSerializer(serializers.ModelSerializer):
  chatobjects = ChatObjectSerializer(many=True, read_only=True)
  class Meta:
    model = ChatRoom
    fields = '__all__'

class FriendSerializer(serializers.ModelSerializer):
  members = UserSerializer(many=True, read_only=True)
  class Meta:
    model = Friend
    fields = '__all__'
    read_only_fields = ['chatroom',]
  
  def create(self, validated_data):
    chatroom = ChatRoom.objects.create()
    friend = Friend.objects.create(chatroom=chatroom)
    chatroom.save(), friend.save()
    members = self.context.get('members', [])
    if len(members) > 0:
      friend.members.set(members)
    return friend


class GroupSerializer(serializers.ModelSerializer):
  members = UserSerializer(many=True, read_only=True)
  class Meta:
    model = Group
    fields = ('id', 'description', 'name', 'status', 'members', 'admins', 'created_at')
  
  def create(self, validated_data):
    chatroom = ChatRoom.objects.create()
    group = Group.objects.create(chatroom=chatroom, **validated_data)
    chatroom.save(), group.save()
    members = self.context.get('members', [])
    if len(members) > 0:
      group.members.set(members)
    return group

class GroupMemberShipSerializer(serializers.ModelSerializer):
  class Meta:
    model = GroupMemberShip
    fields = '__all__'
