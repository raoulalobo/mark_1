from django.db import models

# Create your models here.
class Personne(models.Model):
    GENRE = (
        ('F', 'Feminin'),
        ('M', 'Masculin'),
    )
    dateheure = models.DateTimeField( auto_now=False, blank=True, null=True  )
    nom = models.CharField( max_length=100, unique=True  )
    date_naissance = models.DateField( auto_now=False, auto_now_add=False, blank=True, null=True)
    genre = models.CharField( max_length=1, choices=GENRE) 
    cni = models.CharField( max_length=100, blank=True, null=True )
    telephone = models.CharField( max_length=100, blank=True, null=True )
    observation = models.TextField()

    def __str__(self):
        return '{}'.format( self.nom )

    class Meta:
        ordering = ["nom"]
        abstract = True

        