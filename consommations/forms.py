import re
from django import forms
from consommations.models import Consommation
#from clients.models import Client
from django.core.exceptions import ValidationError

#A quoi la ligne en dessous sert ?
from django.utils.translation import gettext_lazy as _

#La ligne en dessous va me servir de pense bete.
#from django.forms import ClearableFileInput , Textarea, TextInput, ChoiceField

class ConsommationForm(forms.ModelForm):

    class Meta:
        model = Consommation
        
        fields = '__all__'
        labels = {
            'dateheure':_('Date du voyage'),
            #'accueil':'Avez vous ete acceuilli par hotesse ?' ,
        }
        help_texts = {
            #'accueil': _('Exemple : 699999999-John Doe'),
        }
        widgets = {
            'dateheure' : forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}) ,
            'immatriculation' : forms.Select(attrs={'class': 'selectpicker', 'data-live-search':'true', 'data-width':'100%'}) ,
            'consommation': forms.TextInput(attrs={'class': 'form-control'}),
        }
