from dataclasses import field
from pyexpat import model
from django.contrib import admin
from .models import Event



class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['event_name', 'id']    
    

admin.site.register(Event,EventAdmin)


