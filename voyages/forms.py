import re
from django import forms
from voyages.models import Voyage
#from clients.models import Client
from django.core.exceptions import ValidationError

#A quoi la ligne en dessous sert ?
from django.utils.translation import gettext_lazy as _

#La ligne en dessous va me servir de pense bete.
#from django.forms import ClearableFileInput , Textarea, TextInput, ChoiceField

class VoyageForm(forms.ModelForm):

    class Meta:
        model = Voyage
        
        #fields = '__all__'
        exclude = ['revenus']
        labels = {
            'dateheure':_('Date du voyage'),
            #'accueil':'Avez vous ete acceuilli par hotesse ?' ,
        }
        help_texts = {
            #'accueil': _('Exemple : 699999999-John Doe'),
        }
        widgets = {
            'dateheure' : forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}) ,
            'vehicule' : forms.Select(attrs={'class': 'selectpicker', 'data-live-search':'true', 'data-width':'100%'}) ,
            'chauffeur' : forms.Select(attrs={'class': 'selectpicker', 'data-live-search':'true', 'data-width':'100%'}) ,
            'hotesse' : forms.Select(attrs={'class': 'selectpicker', 'data-live-search':'true', 'data-width':'100%'}) ,
            'destination': forms.Select(attrs={'class': 'form-control'}),
            'prix': forms.TextInput(attrs={'class': 'form-control'}),
            'nbr_de_places': forms.TextInput(attrs={'class': 'form-control'}),
            'billet_gratuit': forms.TextInput(attrs={'class': 'form-control'}),
            'consommation': forms.TextInput(attrs={'class': 'form-control'}),
        }
