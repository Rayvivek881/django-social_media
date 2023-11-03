from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.

class CloudinaryData(models.Model):
  link = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)

  def __str__(self):
    return self.name