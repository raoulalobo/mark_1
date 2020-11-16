
import django_filters
from django import forms
from .models import Voyage
from django.db import models



class VoyageFilter(django_filters.FilterSet):

    date_lte = django_filters.DateTimeFilter(field_name='dateheure', 
    lookup_expr='gte' , 
    label='Date debut' , 
    widget=forms.DateTimeInput(attrs={'class': 'form-control flatpickr', 'placeholder':'Date de debut'})
    )
    
    date_gte = django_filters.DateTimeFilter(field_name='dateheure', 
    lookup_expr='lte' , 
    label='Date fin' , 
    widget=forms.DateTimeInput(attrs={'class': 'form-control flatpickr', 'placeholder':'Date de fin'})
    )
    vehicule = django_filters.CharFilter(label='Vehicule', 
    lookup_expr='icontains',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Vehicule'})
    )
    chauffeur = django_filters.CharFilter(label='Chauffeur', 
    lookup_expr='icontains',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Chauffeur'})
    )

    

    class Meta :
        model = Voyage
        fields = ['vehicule', 'chauffeur']