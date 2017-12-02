"""
Definition of models.
"""

from django.db import models
class Pet(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    data_of_birth = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo = models.FileField()

    def __str__(self):
        return self.name
