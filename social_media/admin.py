from django.contrib import admin

# Register your models here.

from .models import ChatObject, ChatRoom, Friend, Group, GroupMemberShip

admin.site.register(ChatObject)
admin.site.register(ChatRoom)
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(GroupMemberShip)