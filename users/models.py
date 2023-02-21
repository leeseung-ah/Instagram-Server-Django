from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
     profileImg = models.URLField(blank=True)
     followNum = models.PositiveIntegerField(default=0)
     profileIntroduce = models.CharField(max_length=150, default="")