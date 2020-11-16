from .models import Vehicule
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class VehiculeResource(resources.ModelResource):

    class Meta:
        model = Vehicule


class VehiculeAdmin(ImportExportModelAdmin):

    resource_class = VehiculeResource

    #Grappeli
    change_list_filter_template = "admin/filter_listing.html"
    #La ligne en dessous ajoute un barre laterale qui fait disparaitres django export_import
    #change_list_template = "admin/change_list_filter_sidebar.html"
    list_display = ['immatriculation', 'sieges']
    list_filter = ['immatriculation', 'sieges']


admin.site.register( Vehicule, VehiculeAdmin)
