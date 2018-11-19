from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    dogs = models.ManyToManyField(to="pets.Dog")

    def __str__(self):
        return self.name
