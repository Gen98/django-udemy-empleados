from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Empleado
from .forms import EmpleadoForm

# Requerimientos
# 1.- lista de todos los empledos de la empresa
# 2.- listar todos los empleados que pertenecen a un area de la empresa
# 3.- listar empleados por trabajo
# 4.- listar todos los empleados por palabra clave
# 5.- listar habilidades de un empleado

class IndexView(TemplateView):
    """ pagina de inicio """
    template_name = 'index.html'

# Create your views here.
class ListaAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    paginate_by = 4 #PAGINACIONES con el parametro page en la ruta, cambiamos los registros 
    # En el html is_paginated PODEMOS Obtener SI ESTA PAGINAO O NO
    ordering = "first_name"
    # model = Empleado # Al hacer uso del get queryset, porque vamos a hacer un filtrado en la pagina, ya no necesitamos esta linea
    context_object_name='empleados' #Se usa este para no darle nombre al objects_list del html

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave # icontains va a hacer una busqueda de lo buscado en el kword en el full name de todos los empleaods  
            # Si kword esta vacio traera todos los empleados          
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'empleado/lista_empleados.html'
    paginate_by = 10 #PAGINACIONES con el parametro page en la ruta, cambiamos los registros 
    # En el html is_paginated PODEMOS Obtener SI ESTA PAGINAO O NO
    ordering = "first_name"
    model = Empleado 
    context_object_name='empleados' #Se usa este para no darle nombre al objects_list del html

class ListaByAreaEmpresa(ListView):
    """ Lista empleados de un area """
    template_name = 'empleado/list_by_area.html'
    context_object_name='empleados'

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista

class ListaEmpleadosByKeyword(ListView):
    """ Lista empleado por palabra clave """
    template_name = 'empleado/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista

class ListaHabilidadesEmpleado(ListView):
    template_name = 'empleado/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=2)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = "empleado/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/add.html"
    form_class = EmpleadoForm #se comentan los field sya que se hara uso de un Form
    # fields = [
    #     'first_name', 
    #     'last_name', 
    #     'job',
    #     'departamento',
    #     'habilidades',
    #     'avatar'
    # ] #Asi se indica campo por campo
    # fields = ('__all__') #asi se indica todos los campos del modelo
    # success_url = 'success' #ruta a redireccionar despues de guardado exitoso
    success_url = reverse_lazy('empleado_app:empleados_admin') #con reverse_lazy se usa el name de la ruta, como laravel Route->name()

    def form_valid(self, form):
        # Esta funcion sire para validar el form de la vista, aqui llenaremos el nombre completo sin pedirlo en la vista
        #Esta funcion  es ya que el formmulario esta validado
        empleado = form.save() #form.save() guarda directamente en la base de datos
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name #Hacemos el fullname
        empleado.save() #Actualizamos la base de datos
        print(empleado)
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url = reverse_lazy('empleado_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        # post sirve para interceptar los datos antes de que sean validados, se ejecuta primero
        self.object = self.get_object()
        print('*******METODO POST********')
        print(request.POST)
        print(request.POST['last_name']) #Asi se obtienen los datos del form
        print('***************')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Form valid sirve para interceptar los datos cuando el form ya esta validado
        print('*******METODO FORM VALID********')

        print('***************')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/delete.html"
    success_url = reverse_lazy('empleado_app:empleados_admin')