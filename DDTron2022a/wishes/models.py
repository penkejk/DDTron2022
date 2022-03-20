from django.db import models
from events.models import Event
from people.models import Person

# Create your models here.



class Wish(models.Model):
    wish_text = models.TextField()    
    author = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='author_rel')
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    assigned_to = models.ForeignKey(Person, on_delete=models.DO_NOTHING, default=None, related_name='assigned_rel', blank=True, null=True)


