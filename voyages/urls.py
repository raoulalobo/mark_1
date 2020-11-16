from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'voyages'
urlpatterns = [

    path('list/', views.list, name='voyages.list'),
    path('add/', views.add, name='voyages.add'),
    path('rapport/', views.rapport, name='voyages.rapport'),
    path('update/<item_id>', views.update, name='voyages.update'),
    #path('add/', views.add_client, name='add.client'),
    #path('delete/<client_id>', views.delete_client, name='delete.client'),
    #path('details/<client_id>', views.details_client, name='details.client'),
]