from email.policy import default
from django.db import models
from django.forms import CharField



class Event(models.Model):
    event_name = models.CharField(max_length=150)
    desciption = models.TextField()
    

    def __str__(self):
        return f"{self.event_name}"