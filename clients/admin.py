from .models import Client
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class ClientResource(resources.ModelResource):

    class Meta:
        model = Client


class ClientAdmin(ImportExportModelAdmin):

    resource_class = ClientResource

    #Grappeli
    change_list_filter_template = "admin/filter_listing.html"
    #La ligne en dessous ajoute un barre laterale qui fait disparaitres django export_import
    #change_list_template = "admin/change_list_filter_sidebar.html"
    list_display = ['nom', 'date_naissance', 'genre', 'cni', 'telephone', 'observation']
    list_filter = ['nom', 'date_naissance', 'genre', 'cni', 'telephone', 'observation']


admin.site.register(Client, ClientAdmin)