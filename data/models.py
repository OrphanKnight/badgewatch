from django.db import models
# Create your models here.

class Officer(models.Model):
    badgeID=models.CharField(max_length = 20)
    firstName=models.CharField(max_length = 20)
    lastName=models.CharField(max_length = 20)

class Complaint(models.Model):
    categroy=models.CharField(max_length = 50)
    badgeID=models.CharField(max_length = 20)
    firstName=models.CharField(max_length = 20)
    lastName=models.CharField(max_length = 20)
    classification=models.CharField(max_length = 20)
    allegation=models.CharField(max_length = 20)
    finding=models.CharField(max_length = 20)
    



