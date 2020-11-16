
import django_filters
from .models import Client
#from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django.db import models
from django import forms
#import datetime


class ClientFilter(django_filters.FilterSet):

    date_lte = django_filters.DateTimeFilter(field_name='date_ajout', 
    lookup_expr='gte' , 
    label='Date debut' , 
    widget=forms.DateTimeInput(attrs={'class': 'form-control flatpickr', 'placeholder':'Date de debut'})
    )
    
    date_gte = django_filters.DateTimeFilter(field_name='date_ajout', 
    lookup_expr='lte' , 
    label='Date fin' , 
    widget=forms.DateTimeInput(attrs={'class': 'form-control flatpickr', 'placeholder':'Date de fin'})
    )
    nom = django_filters.CharFilter(label='Nom', 
    lookup_expr='icontains',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nom'})
    )
    cni = django_filters.CharFilter(label='CNI', 
    lookup_expr='icontains',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'CNI'})
    )
    telephone = django_filters.CharFilter(label='Telephone', 
    lookup_expr='icontains',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Telephone'})
    )
    

    class Meta :
        model = Client
        fields = ['nom', 'cni','telephone']