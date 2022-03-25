from django.contrib import admin
from django.urls import path
from . import views

def DesdeApps(self):
    print('++++++DESDE APP EMPLEADO')

app_name = "empleado_app"  #esta linea de aqui es para nombrar las rutas, es como un route group de laravel, pero sin que aparezca en el url del navegador

urlpatterns = [
    path('', views.IndexView.as_view()),
    # path('empleado', DesdeApps),
    path(
        'listar-todo-empleados/', 
        views.ListaAllEmpleados.as_view(),
        name='empleados_all'
    ),
    path(
        'listar-empleados-admin/', 
        views.ListaEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
    path(
        'listar-by-area/<shortname>/', #<> se declara el nombre de un parametro
        views.ListaByAreaEmpresa.as_view(),
        name='empleados_area'
    ),
    path('buscar-empleado/', views.ListaEmpleadosByKeyword.as_view()),     #<> se declara el nombre de un parametro
    path('lista-habilidades-empleado/', views.ListaHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>/', #en Detailview el parametro del id, forzosamente debe llamarse pk
        views.EmpleadoDetailView.as_view(),
        name='empleado_detalle'
    ),
    path(
        'add-empleado', 
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
    ),
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),
]
