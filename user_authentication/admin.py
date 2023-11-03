from django.contrib import admin
from .models import UserDetails
# Register your models here.

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
  list_display = ('user', 'phone_number', 'city', 'country', 'Image', 'last_seen', 'user_roll')
  list_per_page = 25
  list_display_links = ('user', 'phone_number')
  ordering = ('-last_seen', '-user_roll')
