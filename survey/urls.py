"""survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

#Gestion des fichiers statiques en dev.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
    path('voyages/', include('voyages.urls')),
    path('employes/', include('employes.urls')),
    path('enquetes/', include('enquetes.urls')),
    path('consommations/', include('consommations.urls')),
    path('', include('account.urls', namespace='account')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
