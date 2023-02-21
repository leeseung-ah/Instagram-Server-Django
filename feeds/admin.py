from django.contrib import admin
from .models import Feed

@admin.register
class FeedAdmin(admin.ModelAdmin):
     list_display = (
          "caption",
          "likesNum",
          "reviewsNum",
     )