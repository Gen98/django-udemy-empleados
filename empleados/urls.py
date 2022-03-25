"""empleados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

#def pruebaUrl(self):
#    print('=================================PROBANDO URLS====================');

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('prueba/', pruebaUrl),
    #incluimos las urls de la app departamento
    path('', include('applications.departamento.urls')),
    #incluimos las urls de la app empleado
    path('', include('applications.empleado.urls')),
    #incluimos las urls de la app home
    path('', include('applications.home.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Con esta linea le especificamos al sistema de rutas de django que tambien genere una ruta para los archivos multimedia definidos en settings
