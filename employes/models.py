from django.db import models
from personnes.models import Personne
# Create your models here.

class Poste(models.Model):
    
    designation = models.CharField( max_length=100, unique=True  )
    description = models.TextField()

    def __str__(self):
        return '{}'.format( self.designation )

    class Meta:
        ordering = ["designation"]


class Employe(Personne):

    poste = models.ForeignKey( Poste, null=True , related_name='poste', on_delete=models.SET_NULL)

