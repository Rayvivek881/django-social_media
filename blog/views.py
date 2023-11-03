from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer
from CustomResponse import SuccessResponse, ErrorResponse
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def like_toggle(request, pk):
  if (request.user.is_anonymous):
    return ErrorResponse('Unauthorized', 
      'You are not logged in', status_code=status.HTTP_401_UNAUTHORIZED)
  post = Post.objects.get(id = pk)
  post.like_toggle(request.user.id)
  return SuccessResponse(post.like_count, 'Post like toggled')

class PostViewSet(viewsets.ViewSet):
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
  def list(self, request):
    filterObject = {}
    for key, val in request.query_params.items():
      filterObject[key] = val
    queryset = Post.objects.filter(**filterObject)
    serializer = PostSerializer(queryset, many=True)
    return SuccessResponse(serializer.data, 'Posts retrieved successfully')

  def create(self, request):
    print(request.data)
    serializer = PostSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save(author=request.user)
      return SuccessResponse(serializer.data, 
            'Post created successfully', status.HTTP_201_CREATED)
    return ErrorResponse(serializer.errors, 'Post could not be created')

  def retrieve(self, request, pk=None):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post)
    return SuccessResponse(serializer.data, 'Post retrieved successfully')
 
  def partial_update(self, request, pk=None):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save(author=request.user)
      return SuccessResponse(serializer.data, 'Post updated successfully')
    return ErrorResponse(serializer.errors, 'Post could not be updated')

  def destroy(self, request, pk=None):
    post = Post.objects.get(id=pk)
    post.delete()
    return SuccessResponse(None, 'Post deleted successfully')

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  def create(self, request):
    serializer = CommentSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    serializer.save(author=request.user)
    return SuccessResponse(serializer.data, 
      'Comment created successfully', status.HTTP_201_CREATED)
    