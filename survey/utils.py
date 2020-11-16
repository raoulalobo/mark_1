import random
import string
import socket
import datetime
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.cache import cache
from django.shortcuts import redirect
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def redis_set( request, req_filter, redis , dossier ):

    redis = ''
    redis = redis + request.session['_auth_user_hash'] + '_' + socket.gethostname() + '_' + dossier
    print('--redis--: {}'.format( redis ) )

    cache.set( redis , req_filter.qs , timeout=CACHE_TTL)

def redis_get( request , redis , dossier ):

    redis = ''
    redis = redis + request.session['_auth_user_hash'] + '_' + socket.gethostname() + '_' + dossier

    items = cache.get(redis)

    return items

def liste(request , model , model_filter , dossier , redis ):
 

    all_items = model.objects.all()
    today_items = model.objects.all().filter( dateheure__gte=datetime.date.today() ) 

    req_get = request.GET
    req_get_list_key = list(req_get.keys())
    req_get_list_value = list(req_get.values())
    req_get_list_len = len(req_get_list_key)

    req_session = request.session

    
    if req_get_list_len > 0 :

        date_lte = len( req_get.get('date_lte') )
        date_gte = len( req_get.get('date_gte') )

        # Si les keys values existent ca veut dire q on clique sur la recherche    
        if (  date_lte == 0 ) and ( date_gte == 0 ):
        # Si les champs dates sont vides filtrer les donnees sur la date du jour
            req_filter = model_filter( request.GET , queryset= today_items )
        else:  
            req_filter = model_filter( request.GET , queryset= all_items )
            
        request.session['req_get'] = request.GET


    if ( req_get_list_len == 0 ) and (  'req_get' not in request.session ):
        # Si les keys values existent pas et qu'il y a pas de session req_pneu filter sur la date du jour
        # cas utilisation : retour vers la liste principale suite a un ajout, modification ou sppression apres recherche
        req_filter = model_filter( request.GET , queryset= today_items )


        
    if ( req_get_list_len == 0 ) and (  'req_get' in request.session ):
        # Cas utilisation : Retour vers la liste principale suite a un ajout , modification ou suppression apres recherche    
        req_filter = model_filter( request.session['req_get'] , queryset= all_items )

    redis_set(request, req_filter, redis, dossier)
 
    #--req_filter contient un liste d'elements ( req_filter.qs )ainsi que un fornulaire ( req_filter.form.media )
    # for item in req_filter.qs

    return render(request,'{}/list.html'.format( dossier ),{ 'req_filter' : req_filter })



# --request-- c'est le request que l'on retrouve lors de la declaration d'une vue
# --formulaire-- c'est le ModelForm
# --formulaire_scan-- c'est le ModelForm du 
def ajout_sans_fichier_joint( request ,formulaire, app ,dossier  ):

    if request.method == 'POST':
        form = formulaire(request.POST )
        if form.is_valid() :
            item = form.save()
            messages.success( request,'Item has been added')
            #return redirect(redirection)
            return redirect('{}:{}.list'.format( app , dossier )) 
    else:
        form = formulaire()
  

    #return form , file_form
    return render(request,'{}/add.html'.format( dossier ),{'form': form , 'update': False , 'titre' : dossier })

def maj_sans_fichier_joint( request, _id , modele ,formulaire , app, dossier ) :
    
    #Requetes sur modeles
    item = modele.objects.get( pk = _id )
    #Formulaires
    form = formulaire(request.POST or None, instance= item )
    
    if form.is_valid() :
        item = form.save()         
        messages.success( request,'Item has been updated')
        return redirect('{}:{}.list'.format( app , dossier))
    else:
        form = formulaire( None,  instance=item )


    return render(request, '{}/add.html'.format( dossier), { 'form': form , 'item': item, 'update': True , 'titre': dossier })

def suppression_sans_fichier_joint( request , _id , modele , app , dossier ) :

    item = modele.objects.get( pk = _id )
    item.delete()
    messages.success( request,('Item has been deleted') )
    return redirect('{}:{}.list'.format( app , dossier ))

