from django.db import models

# Create your models here.


class Event(models.Model):
    eventName = models.CharField(max_length=50, blank=False, null=False)
    eventDescription = models.TextField(max_length=100, blank=False, null=False)
    eventLocation = models.CharField(max_length=50, blank=False, null=False)
    eventCapacity = models.PositiveIntegerField(blank=False, null=False)
    eventDate = models.DateField()
    eventPoster = models.ImageField(upload_to="eventposters/", blank=False, null=False)
    eventCost = models.PositiveIntegerField(blank=False, null=False)
    facebook = models.CharField(max_length=500, blank=True, null=True)
    twitter = models.CharField(max_length=500, blank=True, null=True)
    instagram = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.eventName


