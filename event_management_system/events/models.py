# events/models.py
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location_name = models.CharField(max_length=255)
    available_slots = models.PositiveIntegerField(default=0)
    
    @classmethod
    def search_events(cls, query):
        return cls.objects.filter(
            models.Q(title__icontains=query) |
            models.Q(description__icontains=query) |
            models.Q(location_name__icontains=query)
        )
    
    def __str__(self):
        return self.title

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user}'
