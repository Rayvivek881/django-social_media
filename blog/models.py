from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
  content = models.TextField(default='')
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey('Post', on_delete=models.CASCADE)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
  content = models.TextField()
  title = models.CharField(max_length=100)
  image = models.CharField(max_length=100, blank=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  likes = models.ManyToManyField(User, related_name='likes', blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created_at', '-updated_at']
  
  @property
  def like_count(self):
    return self.likes.count()
  
  @property
  def comment_count(self):
    return Comment.objects.filter(post=self).count()
  
  def like_toggle(self, user_id):
    user = User.objects.get(id=user_id)
    if user in self.likes.all():
      self.likes.remove(user)
    else: self.likes.add(user)
  
  def is_liked(self, user_id):
    user = User.objects.get(id=user_id)
    return user in self.likes.all()
  
  def set_author(self, user_id):
    self.author = User.objects.get(id=user_id)
    self.save()

  def __str__(self):
    return f'{self.title} by {self.author.username}'