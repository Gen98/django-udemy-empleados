from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"  #esta linea de aqui es para nombrar las rutas, es como un route group de laravel, pero sin que aparezca en el url del navegador

urlpatterns = [
    path(
        'departamento-lista/',
        views.DepartamentoListView.as_view(),
        name='departamento_list'
    ),
    path(
        'new-departamento/', 
        views.NewDepartamentoView.as_view(),
        name='nuevo_departamento'
    ),
]
