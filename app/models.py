"""
Definition of models.
"""

from django.db import models
GENDER_CHOICE = (('m', 'M'), ('f', 'F'))
CHARACTER_CHOICE = (('calm', 'Calm'), ('friendly', 'Friendly'), ('defender', 'Defender'), ('hunter', 'Hunter'), ('playful', 'playful'))
TYPE_CHOICE = (('dog', 'Dog'), ('cat', 'Cat'))

class Pet(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICE)
    breed = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICE)
    character = models.CharField(max_length=10, choices=CHARACTER_CHOICE)
    date_of_birth = models.DateField()
    condition = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_person_id = models.CharField(max_length=100)
<<<<<<< HEAD
    photo = models.ImageField()
=======
    photo = models.ImageField(upload_to='pets', default='media/default.jpg')
>>>>>>> 6f5b886fc5f3bf5c0bc48fbf60cc28264a837d14

    def __str__(self):
        return self.name
