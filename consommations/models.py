from django.db import models
from vehicules.models import Vehicule
from employes.models import Employe

# Create your models here.
class Consommation(models.Model):

    dateheure = models.DateTimeField( auto_now=False, auto_now_add=False )
    immatriculation = models.ForeignKey( Vehicule, null=True , on_delete=models.SET_NULL)
    consommation= models.DecimalField( default = 0 , max_digits=6, decimal_places=2 )

    def __str__(self):
        return '{}'.format( self.immatriculation  )

    class Meta:
        ordering = ["dateheure"]