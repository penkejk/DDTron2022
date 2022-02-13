from django.db import models
from django.forms import CharField

# Create your models here.
class Person(models.Model):
    name = CharField(max_length=100)
