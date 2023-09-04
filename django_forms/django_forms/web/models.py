from django.db import models

class Pet(models.Model):
    name = models.CharField(
        max_length=30,
    )


# Create your models here.
class Person(models.Model):
    MAX_NAME_LENGTH = 30
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,

    )
    age = models.PositiveIntegerField(

    )
    pets = models.ManyToManyField(
        Pet,
    )
