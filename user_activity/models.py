from django.contrib import auth
from django.db import models
from django.utils import timezone


class User(models.Model):
    id=models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    real_name=models.CharField(max_length=50, blank=False, null=False)
    tz=models.CharField(max_length=50, blank=False, null=False)

class UserActivity(models.Model):
    user = models.ForeignKey(User, related_name='activity_periods', on_delete=models.CASCADE)
    start_time= models.DateTimeField()
    end_time= models.DateTimeField()
