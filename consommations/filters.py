
import django_filters
from django import forms
from .models import Consommation
from django.db import models



class ConsommationFilter(django_filters.FilterSet):

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
    immatriculation = django_filters.CharFilter(label='Immatriculation', 
    lookup_expr='icontains',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Immatriculation'})
    )
    consommation = django_filters.CharFilter(label='Consommation', 
    lookup_expr='icontains',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Consommation'})
    )


    class Meta :
        model = Consommation
        fields = ['immatriculation', 'consommation']