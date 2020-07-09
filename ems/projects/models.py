from django.db import models
from django.contrib.postgres.fields import ArrayField

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Sample(models.Model):
    name = models.CharField(max_length=33)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_created = models.DateField()
    number_of_layers = models.IntegerField()
    layers = ArrayField(models.CharField(max_length=15))
    substrate = models.CharField(max_length=33)
    thickness = ArrayField(models.IntegerField())

    def __str__(self):
        return  self.name

class Machine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return  self.name

class Measurement(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return  self.name

class Experiment(models.Model):
    name = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    date_measured = models.DateField()
    def __str__(self):
        return  self.name

class User(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=31)

    def __str__(self):
        return self.user_name
