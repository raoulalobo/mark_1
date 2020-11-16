from .models import Enquete
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class EnqueteResource(resources.ModelResource):

    class Meta:
        model = Enquete


class EnqueteAdmin(ImportExportModelAdmin):

    resource_class = EnqueteResource

    #Grappeli
    change_list_filter_template = "admin/filter_listing.html"
    #La ligne en dessous ajoute un barre laterale qui fait disparaitres django export_import
    #change_list_template = "admin/change_list_filter_sidebar.html"
    list_display = ['voyage', 'client', 'accueil', 'presentation', 'politesse', 'sourire', 'professionnelle', 'nbr_passages', 'speech_de_depart', 'speech_controles_police', 'speech_entree_ville', 'speech_points_arrets', 'speech_bilingue', 'odeur', 'nettoyage_final']
    list_filter = ['voyage', 'client', 'accueil', 'presentation', 'politesse', 'sourire', 'professionnelle', 'nbr_passages', 'speech_de_depart', 'speech_controles_police', 'speech_entree_ville', 'speech_points_arrets', 'speech_bilingue', 'odeur', 'nettoyage_final']


admin.site.register( Enquete, EnqueteAdmin )