from django.contrib import admin
from .models import Comment, Post

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('content', 'author', 'post', 'created_at', 'updated_at')
  list_per_page = 25
  ordering = ('-updated_at', '-created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'image', 'author', 'created_at', 'like_count', 'comment_count')
  list_per_page = 25
  list_display_links = ('title', 'id')
  ordering = ('-updated_at', '-created_at')