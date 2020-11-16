from django.db import models
from voyages.models import Voyage
from clients.models import Client
from datetime import datetime, timezone
from django.utils import timezone
# Create your models here.

class Enquete(models.Model):


    REPONSE = (
        ('O', 'Oui'),
        ('N', 'Non'),
        ('A', 'Abstention'),
    )
    dateheure = models.DateTimeField( default = timezone.now )
    voyage = models.ForeignKey( Voyage, null=True , related_name='voyage', on_delete=models.SET_NULL)
    client = models.ForeignKey( Client, null=True , related_name='client', on_delete=models.SET_NULL)
    accueil = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2])
    presentation = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2] ) 
    politesse = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2]) 
    sourire = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2] ) 
    professionnelle = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2] ) 
    nbr_passages = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2]) 
    speech_de_depart = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2] ) 
    speech_controles_police = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2] ) 
    speech_entree_ville = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2] ) 
    speech_points_arrets = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2] ) 
    speech_bilingue = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2] ) 
    odeur = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2] ) 
    nettoyage_final = models.CharField( max_length=1, choices=REPONSE, default=REPONSE[2] ) 

    def __str__(self):
        return '{}-{}'.format( self.voyage, self.client )

    class Meta:
        ordering = ["voyage__dateheure"]   
