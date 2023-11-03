from collections.abc import Collection
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

rolls = ['user', 'admin', 'superadmin', 'owner']

class UserDetails(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone_number = models.CharField(max_length=10, blank=True, null=True)
  city = models.CharField(max_length=50, blank=True, null=True)
  country = models.CharField(max_length=50, default='India')
  Image = models.CharField(blank=True, null=True, max_length=500)
  last_seen = models.DateTimeField(blank=True, null=True)
  user_roll = models.CharField(max_length=20, default='user')

  @property
  def full_name(self):
    return f"{self.user.first_name} {self.user.last_name}"
  
