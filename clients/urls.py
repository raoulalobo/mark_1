from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'clients'
urlpatterns = [

    #client
    path('accueil/', views.accueil, name='accueil.client'),
    #path('list/', views.list_client, name='list.client'),
    #path('add/', views.add_client, name='add.client'),
    #path('delete/<client_id>', views.delete_client, name='delete.client'),
    #path('update/<client_id>', views.update_client, name='update.client'),
    #path('details/<client_id>', views.details_client, name='details.client'),
]