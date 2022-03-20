from django.db import models

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=200)
    

class Person(models.Model):
    person_name = models.CharField(max_length=200)
    person_email = models.EmailField(unique=True)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, default=None)