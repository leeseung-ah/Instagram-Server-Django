from django.db import models
from common.models import CommonModel

class Review(CommonModel):
     caption = models.CharField(max_length=150)
     
     
     
