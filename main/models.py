from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Cities(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User)
