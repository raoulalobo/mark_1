from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'enquetes'
urlpatterns = [

    #enquetes
    path('list/', views.list, name='enquetes.list'),
    path('add/', views.add, name='enquetes.add'),
    #path('delete/<client_id>', views.delete_client, name='delete.client'),
    #path('update/<client_id>', views.update_client, name='update.client'),
    #path('details/<client_id>', views.details_client, name='details.client'),
]