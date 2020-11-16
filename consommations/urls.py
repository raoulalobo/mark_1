from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'consommations'
urlpatterns = [

    path('list/', views.list, name='consommations.list'),
    path('add/', views.add, name='consommations.add'),
    path('update/<item_id>', views.update, name='consommations.update'),
    #path('add/', views.add_client, name='add.client'),
    #path('delete/<client_id>', views.delete_client, name='delete.client'),
    #path('details/<client_id>', views.details_client, name='details.client'),
]