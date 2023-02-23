from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
     profileImg = models.URLField(blank=True)
     followerNum = models.PositiveIntegerField(default=0)
     profileIntroduce = models.CharField(max_length=150, default="")