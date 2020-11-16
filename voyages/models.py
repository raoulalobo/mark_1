from django.db import models
from vehicules.models import Vehicule
from employes.models import Employe

class DoualaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(destination='D')

class YaoudeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(destination='Y')

class VilleManager(models.Manager):

    def yaounde(self, keyword):
        return self.filter(destination='Y') #.count()

    def douala(self, keyword):
        return self.filter(destination='D') #.count()


# Create your models here.
class Voyage(models.Model):
    
    DESTINATION = (
        ('D', 'Douala'),
        ('Y', 'Yaounde'),
    )
    dateheure = models.DateTimeField( auto_now=False, auto_now_add=False )
    vehicule = models.ForeignKey( Vehicule, null=True , related_name='bus', on_delete=models.SET_NULL)
    chauffeur = models.ForeignKey( Employe, null=True , related_name='chauffeur', on_delete=models.SET_NULL, limit_choices_to={'poste': 2 }, )
    hotesse = models.ForeignKey( Employe, null=True , related_name='hotesse', on_delete=models.SET_NULL , limit_choices_to={'poste': 1 }, )
    destination = models.CharField( max_length=1, choices=DESTINATION) 
    prix = models.PositiveIntegerField( default = 0 )
    nbr_de_places = models.PositiveIntegerField( default = 0 )
    billet_gratuit = models.PositiveIntegerField( default = 0)
    revenus = models.PositiveIntegerField( default = 0)
    consommation= models.DecimalField( default = 0 , max_digits=6, decimal_places=2 )

    objects = VilleManager() ## Voyage.objetcs.all()
    douala = DoualaManager()   ## Voyage.douala.all()
    yaounde = YaoudeManager()  ## Voyage.yaounde.all()

    

    def __str__(self):
        return '{}-{}-{}'.format( self.dateheure, self.vehicule , self.chauffeur )

    class Meta:
        ordering = ["dateheure"]

    
    #def revenus(self):
    #    nbr_de_places = self.nbr_de_places
    #    billet_gratuit = self.billet_gratuit
    #    prix = self.prix
    #    total = ( nbr_de_places - billet_gratuit ) * prix
    #    #print(total)
    #
    #    return total

    #@property
    #def revenus(self):
    #    nbr_de_places = self.nbr_de_places
    #    billet_gratuit = self.billet_gratuit
    #    prix = self.prix
    #    total = ( nbr_de_places - billet_gratuit ) * prix
    #    #print(total)
    #
    #    return total
    
    def save(self, *args, **kwargs):

        prix = self.prix
        nbr_de_places = self.nbr_de_places
        billet_gratuit = self.billet_gratuit
        revenus = ( nbr_de_places - billet_gratuit ) * prix

        self.revenus = revenus

        super().save(*args, **kwargs)  # Call the "real" save() method.
