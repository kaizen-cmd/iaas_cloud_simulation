from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Container(models.Model):

    creator = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="containers")
    container_id = models.CharField(max_length=255)
    port = models.IntegerField(default=5000)
    created_on = models.DateTimeField(auto_now=True)
