from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Officer(models.Model):
    badgeID=models.CharField(max_length = 100)
    firstName=models.CharField(max_length = 100)
    lastName=models.CharField(max_length = 100)

