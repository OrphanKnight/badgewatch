from django.db import models
# Create your models here.

class Officer(models.Model):
    badgeID=models.IntegerField(primary_key=True)
    firstName=models.CharField(max_length = 20)
    lastName=models.CharField(max_length = 20)
    

class Complaint(models.Model):
    category=models.CharField(null=True, max_length = 50)
    badgeID_id=models.ForeignKey(Officer, on_delete=models.CASCADE)
    classification=models.CharField(null=True, max_length = 50,)
    allegation=models.CharField(null=True, max_length = 50)
    finding=models.CharField(null=True, max_length = 50 )
    
