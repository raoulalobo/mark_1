from django import forms
from .models import Enquete
from clients.models import Client
from voyages.models import Voyage
from django import forms
#from django.forms import ClearableFileInput , Textarea, TextInput, ChoiceField
#from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
import re

#from dal import autocomplete , forward


from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class EnqueteForm(forms.ModelForm):

    #voyage = forms.ModelChoiceField( queryset=Voyage.objects.all() )
    #client = forms.ModelChoiceField( queryset=Client.objects.all() , widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search':'true', 'data-width':'100%'}) )
    #client = forms.ModelChoiceField( queryset=Client.objects.all() , widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search':'true', 'data-width':'100%'}) )
    class Meta:
        model = Enquete
        
        fields = ( 'voyage', 'client','accueil', 'presentation', 'politesse', 'sourire', 'professionnelle','nbr_passages', 'speech_de_depart', 'speech_controles_police', 'speech_entree_ville', 'speech_points_arrets', 'speech_bilingue', 'odeur', 'nettoyage_final' )
        #fields =()
        labels = {
            #'politesse':_('Money'),
            'accueil':'Avez vous ete acceuilli par hotesse ?' ,
        }
        help_texts = {
            #'accueil': _('Exemple : 699999999-John Doe'),
        }
        widgets = {
            'voyage' : forms.Select(attrs={'class': 'selectpicker', 'data-live-search':'true', 'data-width':'100%'}) ,
            'client' : forms.Select(attrs={'class': 'selectpicker', 'data-live-search':'true', 'data-width':'100%'}) ,
            'accueil': forms.Select(attrs={'class': 'form-control'}),
            'presentation': forms.Select(attrs={'class': 'form-control'}),
            'politesse': forms.Select(attrs={'class': 'form-control'}),
            'sourire': forms.Select(attrs={'class': 'form-control'}),
            'professionnelle': forms.Select(attrs={'class': 'form-control'}),
            'nbr_passages': forms.Select(attrs={'class': 'form-control'}),
            'speech_de_depart': forms.Select(attrs={'class': 'form-control'}),
            'speech_controles_police': forms.Select(attrs={'class': 'form-control'}),
            'speech_entree_ville': forms.Select(attrs={'class': 'form-control'}),
            'speech_points_arrets': forms.Select(attrs={'class': 'form-control'}),
            'speech_bilingue': forms.Select(attrs={'class': 'form-control'}),
            'odeur': forms.Select(attrs={'class': 'form-control'}),
            'nettoyage_final': forms.Select(attrs={'class': 'form-control'}),
            #'accueil': forms.Select(attrs={'class': 'form-control'}),
            #'libelle': autocomplete.ModelSelect2(url='country-autocomplete')
            #'immatriculation': AutoCompleteSelectMultipleField('cars', required=False, help_text=None)
            #'numero_colis': Textarea(attrs={'cols': 80, 'rows': 20, 'readonly': True}),
            #'dateheure': DateTimePickerInput(), # default date-format %m/%d/%Y will be used
        }
