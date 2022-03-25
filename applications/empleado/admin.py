from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin): #Clase de django para modificar la vista del modelo en el administrador
    #list display solo muestra atributos del modelo, si no es del modelo se declara una funcion como full name por ejemplo
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name'
    )
    #
    def full_name(self, obj):
        #obj es cada iteracion del modelo
        #print(obj)
        return obj.first_name + ' ' + obj.last_name
    #
    search_fields = ('first_name',)
    list_filter = ( 'departamento', 'job', 'habilidades') #agrega el cuadrito de filtro
    filter_horizontal = ('habilidades',) #Este filtro solo sirve para relaciones

admin.site.register(Empleado, EmpleadoAdmin) #Agregamos la clase de la vista admin
admin.site.register(Habilidades)
