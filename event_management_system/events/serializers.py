from rest_framework import serializers
from .models import Event, Registration

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    
    event_title = serializers.CharField(source='event.title', read_only=True)
    event_date = serializers.CharField(source='event.date', read_only=True)
    event_time = serializers.CharField(source='event.time', read_only=True)
    event_location_name = serializers.CharField(source='event.location_name', read_only=True)
    
    
    class Meta:
        model = Registration
        fields = '__all__'
