from .models import Employe , Poste
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class EmployeResource(resources.ModelResource):

    class Meta:
        model = Employe


class EmployeAdmin(ImportExportModelAdmin):

    resource_class = EmployeResource

    #Grappeli
    change_list_filter_template = "admin/filter_listing.html"
    #La ligne en dessous ajoute un barre laterale qui fait disparaitres django export_import
    #change_list_template = "admin/change_list_filter_sidebar.html"
    list_display = ['nom', 'poste', 'date_naissance', 'genre', 'cni', 'telephone', 'observation']
    list_filter = ['nom', 'poste', 'date_naissance', 'genre', 'cni', 'telephone', 'observation']


admin.site.register(Employe, EmployeAdmin)

class PosteResource(resources.ModelResource):

    class Meta:
        model = Poste

    
class PosteAdmin(ImportExportModelAdmin):

    resource_class = PosteResource

    #Grappeli
    change_list_filter_template = "admin/filter_listing.html"
    #La ligne en dessous ajoute un barre laterale qui fait disparaitres django export_import
    #change_list_template = "admin/change_list_filter_sidebar.html"
    list_display = ['designation', 'description']
    list_filter = ['designation', 'description']


admin.site.register(Poste, PosteAdmin)