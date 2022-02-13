from pickle import NONE
from django.db import models
from django.forms import CharField
#from people.models import Person
#from events.models import Event

# Create your models here.


class Wish(models.Model):
    text = CharField(max_length=2000)
    #event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, default=NONE)
    #owner = models.ForeignKey(Person, on_delete=models.DO_NOTHING, default=NONE)


