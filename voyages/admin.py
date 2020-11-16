from .models import Voyage
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class VoyageResource(resources.ModelResource):

    class Meta:
        model = Voyage


class VoyageAdmin(ImportExportModelAdmin):

    resource_class = VoyageResource

    #Grappeli
    change_list_filter_template = "admin/filter_listing.html"
    #La ligne en dessous ajoute un barre laterale qui fait disparaitres django export_import
    #change_list_template = "admin/change_list_filter_sidebar.html"
    list_display = ['dateheure', 'vehicule', 'chauffeur', 'hotesse', 'destination']
    list_filter = ['dateheure', 'vehicule', 'chauffeur', 'hotesse', 'destination']


admin.site.register( Voyage, VoyageAdmin)