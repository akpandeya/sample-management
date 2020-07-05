from django.db import models
from django.contrib.postgres.fields import ArrayField

class project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class sample(models.Model):
    name = models.CharField(max_length=33)
    date_created = models.DateTimeField()
    number_of_layers = models.IntegerField()
    layers = ArrayField(models.CharField(max_length=15))
    substrate = models.CharField(max_length=33)
    thickness = ArrayField(models.IntegerField())

    def __str__(self):
        return  self.name

class experiment():
    name = models.CharField(max_length=255)
    machine = models.CharField(max_length=255)
    date_measured = models.DateTimeField()
    def __str__(self):
        return  self.name
