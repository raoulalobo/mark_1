#import requests
import datetime
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from survey.utils import ajout_sans_fichier_joint
from .forms import EnqueteForm
#from .models import Client
#from .filters import ClientFilter

# Create your views here.

def list(request):

    homeland = 'Accueil ENQUETES'

    return render(request,'enquetes/list.html',{'homeland': homeland } )


def add(request):

    return ajout_sans_fichier_joint(request, EnqueteForm, 'enquetes', 'enquetes')

