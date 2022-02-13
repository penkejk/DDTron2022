from django.db import models
from django.forms import CharField


class Event(models.Model):
    name = CharField(max_length=100)
