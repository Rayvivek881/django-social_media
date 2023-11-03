from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username')

class PostSerializer(serializers.ModelSerializer):
  author = UserSerializer(read_only=True)
  class Meta:
    model = Post
    fields = '__all__'
    read_only_fields = ('author', 'like_count', 'is_liked', 'comment_count')

class CommentSerializer(serializers.ModelSerializer):
  author = UserSerializer(read_only=True)
  class Meta:
    model = Comment
    fields = '__all__'
    read_only_fields = ('author', 'content')