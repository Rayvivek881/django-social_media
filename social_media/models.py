from django.db import models
from django.contrib.auth.models import User

class ChatObject(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  message = models.TextField()

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def is_user(self, user_id):
    user = User.objects.get(id=user_id)
    return user == self.user
  
  def __str__(self) -> str:
    return f'{self.user.username}: message'

class ChatRoom(models.Model):
  chatobjects = models.ManyToManyField(ChatObject, related_name='chatroom', blank=True)

  def add_chatobject(self, user, message):
    chatobject = ChatObject.objects.create(user=user, message=message)
    self.chatobjects.add(chatobject)
  
  def remove_chatobject(self, chatobject_id):
    chatobject = ChatObject.objects.get(id=chatobject_id)
    self.chatobjects.remove(chatobject)
    chatobject.delete()
  
  def __str__(self) -> str:
    return f'Chatroom {self.id}'

class Friend(models.Model):
  members = models.ManyToManyField(User, default=[])
  chatroom = models.OneToOneField(ChatRoom, on_delete=models.CASCADE, null=True)

  def is_friend(self, user_id):
    user = User.objects.get(id=user_id)
    return user in self.members.all()
  
  def __str__(self) -> str:
    return 'Friendship between {}'.format(', '.join([str(m) for m in self.members.all()]))
  
class Group(models.Model):
  description = models.TextField()
  name = models.CharField(max_length=100)
  status = models.CharField(max_length=200, default='public')
  chatroom = models.OneToOneField(ChatRoom, on_delete=models.CASCADE, null=True)

  members = models.ManyToManyField(User, through='GroupMemberShip')
  admins = models.ManyToManyField(User, blank=True, related_name='admin_groups')

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('-created_at', '-updated_at')
  
  def add_member(self, user_id, is_admin=False):
    user = User.objects.get(id=user_id)
    self.members.add(user)
    if is_admin:
      self.admins.add(user)
  
  def remove_member(self, user_id):
    user = User.objects.get(id=user_id)
    self.members.remove(user)
    if user in self.admins.all():
      self.admins.remove(user)
  
  def is_member(self, user_id):
    user = User.objects.get(id=user_id)
    return user in self.members.all()

  def __str__(self):
    return self.name

class GroupMemberShip(models.Model):
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.user.username} is a member of {self.group.name}'