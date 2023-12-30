# events/admin.py
from django.contrib import admin
from .models import Event, Registration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location_name', 'available_slots')
    search_fields = ('title', 'description', 'location_name')
    list_filter = ('date',)

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registration_date')
    search_fields = ('user__username', 'event__title', 'event__location_name')
    list_filter = ('registration_date',)
