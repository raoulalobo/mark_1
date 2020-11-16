from django.db import models
from personnes.models import Personne
# Create your models here.

class Vehicule(models.Model):

    TYPE_DE_VOITURE = (
        ('B', 'Bus'),
        ('P', 'Personnel'),
        ('G', 'Groupe'),
        ('N', 'Navette'),
    )
    dateheure = models.DateTimeField( auto_now=False, blank=True, null=True  )
    immatriculation = models.CharField( max_length=100, unique=True  )
    sieges = models.IntegerField()
    type_de_voiture = models.CharField( max_length=1, choices=TYPE_DE_VOITURE, default= 'B') 

    def __str__(self):
        return '{}'.format( self.immatriculation )

    class Meta:
        ordering = ["immatriculation"]

