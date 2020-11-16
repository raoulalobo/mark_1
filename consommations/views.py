#import requests
import datetime
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .forms import ConsommationForm
from .models import Consommation
from .filters import ConsommationFilter
from survey.utils import liste , ajout_sans_fichier_joint, maj_sans_fichier_joint , redis_get

from django.db.models import Sum , Count 

# Create your views here.

def list(request):

    return liste(request, Consommation , ConsommationFilter , 'consommations' , 'redis_consommations')


def add(request):

    return ajout_sans_fichier_joint(request, ConsommationForm, 'consommations' , 'consommations' )


def update(request, item_id ):

    return maj_sans_fichier_joint(request, item_id , Consommation , ConsommationForm , 'consommations' , 'consommations' )

