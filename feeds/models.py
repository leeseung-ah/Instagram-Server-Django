from django.db import models
from common.models import CommonModel


class Feed(CommonModel):
     contentImg = models.URLField(blank=True)
     likesNum = models.PositiveIntegerField(default=0)
     caption = models.CharField(max_length=1000, default=0)
     reviewsNum = models.CharField(default=0)
          
