from django.db import models

# Create your models here.


class Person(models.Model):
    person_name = models.CharField(max_length=200)
    person_email = models.EmailField(unique=True)