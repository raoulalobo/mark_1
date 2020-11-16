from datetime import datetime
from .models import Voyage
from .forms import VoyageForm
from django.conf import settings
from .filters import VoyageFilter
from django.shortcuts import render
from django.contrib import messages
from django.core.cache import cache
from django.http import JsonResponse
from django.db.models import Sum , Count
from django.shortcuts import render , redirect
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .tasks import rapport_general , rapport_dla , rapport_yde
from django.contrib.auth.decorators import permission_required , login_required
from survey.utils import liste , ajout_sans_fichier_joint, maj_sans_fichier_joint , redis_get

# Create your views here.
@login_required
def list(request):

    return liste(request, Voyage , VoyageFilter , 'voyages' , 'redis_voyages' )

@login_required
def add(request):

    return ajout_sans_fichier_joint( request , VoyageForm, 'voyages' , 'voyages' )

@login_required
def update(request, item_id ):

    return maj_sans_fichier_joint(request, item_id , Voyage , VoyageForm , 'voyages' , 'voyages' )

@login_required
def rapport(request):

    items = redis_get(request, 'redis_voyages', 'voyages')

    vges = items.count()
    recette = items.aggregate( Sum('revenus') )['revenus__sum'] or 0.00
    #revenus__sum est la variable retoutee par l'aggregation , ce nom de variable est attribue 
    #automatiquement par django , il est compose du champ ( ici revenus ) + la fction d'aggregation ( ici sum )
    #la fction d'aggregation retourne un dictinnaire. Expemle : {'price__avg': 34.35}
    #Faire les recherches sur les dictionnaires en python
    
    vges_vip = items.filter( prix__gt = 4000).count()
    recette_vip = items.filter( prix__gt = 4000).aggregate( Sum('revenus') )['revenus__sum'] or 0.00
    
    vges_cla = items.filter( prix__lte = 4000).count()
    recette_cla = items.filter( prix__lte = 4000).aggregate( Sum('revenus') )['revenus__sum'] or 0.00
  
    rapport_general.delay( vges, recette, vges_vip , recette_vip, vges_cla , recette_cla )

    
    #Yaounde

    vges_yde = items.filter( destination='D' ).count()
    recette_yde = items.filter( destination ='D' ).aggregate( somme = Sum('revenus') )['somme'] or 0.00
    
    vges_yde_vip = items.filter(destination='D').filter( prix__gt = 4000).count() 
    recette_yde_vip = items.filter(destination='D').filter( prix__gt = 4000).aggregate( Sum('revenus') )['revenus__sum'] or 0.00
  
    vges_yde_cla = items.filter(destination='D').filter( prix__lte = 4000).count() 
    recette_yde_cla = items.filter(destination='D').filter( prix__lte = 4000).aggregate( Sum('revenus') )['revenus__sum'] or 0.00
  
    rapport_yde(vges_yde, recette_yde, vges_yde_vip, recette_yde_vip, vges_yde_cla, recette_yde_cla)

    #Douala

    vges_dla = items.filter( destination='Y' ).count()
    recette_dla = items.filter( destination ='Y' ).aggregate( somme = Sum('revenus') )['somme'] or 0.00
    

    vges_dla_vip = items.filter(destination='Y').filter( prix__gt = 4000).count() 
    recette_dla_vip = items.filter(destination='Y').filter( prix__gt = 4000).aggregate( Sum('revenus') )['revenus__sum'] or 0.00
  
    vges_dla_cla = items.filter(destination='Y').filter( prix__lte = 4000).count() 
    recette_dla_cla = items.filter(destination='Y').filter( prix__lte = 4000).aggregate( Sum('revenus') )['revenus__sum'] or 0.00

    rapport_dla(vges_dla, recette_dla, vges_dla_vip, recette_dla_vip, vges_dla_cla, recette_dla_cla)

    
    date = datetime.now()

    if date.hour < 10 :
        item = items.first()
        date = item.dateheure 
        heure = date.hour
        heure = date.minute
        print('premier depart. {}:{} ,bus: {}'.format( heure , date.minute , item.vehicule ) )
        premier_depart = 'premier depart. {}:{} ,bus: {}'.format( heure , date.minute , item.vehicule )

    if date.hour > 18 :
        item = items.last()
        date = item.dateheure 
        heure = date.hour
        heure = date.minute
        print('dernier depart. {}:{} ,bus: {}'.format( heure , date.minute , item.vehicule ) )
        dernier_depart = 'dernier depart. {}:{} ,bus: {}'.format( heure , date.minute , item.vehicule ) 

    #print('--dla_count--: {}'.format( dla_count ) )
    #print('--dla_revenus--: {}'.format( dla_revenus ) )
    #print('--dla_revenus_vip--: {}'.format( dla_revenus_vip ) )
    #print('--dla_revenus_class--: {}'.format( dla_revenus_class ) )
    #print('########################################################################')
    #print('--yde_count--: {}'.format( yde_count ) )
    #print('--yde_revenus--: {}'.format( yde_revenus ) )

    #yde_count = colis.filter(destination='DLA').count()
    #yde_montant = colis.filter(destination='DLA').aggregate(Sum('montant'))['montant__sum'] or 0.00
    
    #dla_count = colis.filter(destination='YDE').count()
    #dla_montant =  colis.filter(destination='YDE').aggregate(Sum('montant'))['montant__sum'] or 0.00

    #rapport_created.delay( request.user.id , total_count, total_montant, yde_count, yde_montant, dla_count, dla_montant )
    
    return redirect('voyages:voyages.list')