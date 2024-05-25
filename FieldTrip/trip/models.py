from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#This is global information, everyone can see all the trips
class Trip(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    location = models.TextField()
    deadline = models.DateTimeField(verbose_name="Application Deadline Date")

#You will be able to see all participants on a trip
class TripParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)