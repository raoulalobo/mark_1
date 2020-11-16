#import requests
import datetime
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .models import Client
from .filters import ClientFilter

# Create your views here.

def accueil(request):

    #Implementation elementaire de requete sur Client
    #clients = Client.objects.all()


    pneuss = Client.objects.all()
    pneus = Client.objects.all().filter( date_ajout__gte=datetime.date.today() ) 

    print('-----------request.GET------------------ : ', request.GET )
    req_pneu = request.GET
    req_pneu_list_key = list(req_pneu.keys())
    req_pneu_list_value = list(req_pneu.values())
    req_pneu_list_len = len(req_pneu_list_key)

    req_session = request.session

    
    if req_pneu_list_len > 0 :

        date_lte = len( req_pneu.get('date_lte') )
        date_gte = len( req_pneu.get('date_gte') )

        # Si les keys values existent ca veut dire q on clique sur la recherche    
        if (  date_lte == 0 ) and ( date_gte == 0 ):
        # Si les champs dates sont vides filtrer les donnees sur la date du jour
            pneu_filter = ClientFilter( request.GET , queryset= pneus )
        else:  
            pneu_filter = ClientFilter( request.GET , queryset= pneuss )
            
        request.session['req_coli'] = request.GET


    if ( req_pneu_list_len == 0 ) and (  'req_coli' not in request.session ):
        # Si les keys values existent pas te q il ya pas de session req_pneu filter sur la date du jour
        # cas utilisation : retour vers la liste principale suite a un ajout, modification ou sppression apres recherche
        pneu_filter = ClientFilter( request.GET , queryset= pneus )


        
    if ( req_pneu_list_len == 0 ) and (  'req_coli' in request.session ):
        # Cas utilisation : Retour vers la liste principale suite a un ajout , modification ou suppression apres recherche    
        pneu_filter = ClientFilter( request.session['req_coli'] , queryset= pneuss )


    home = 'home'

    return render(request,'clients/list.html',{'home': home , 'clients' : pneu_filter })