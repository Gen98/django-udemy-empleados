from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm 
from applications.empleado.models import Empleado
from .models import Departamento

# Create your views here.
# La clase de abajo esta relacionada a mas de un modelo, por eso no es una una vista generica como las antes vistas
class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('****ESTAMOS EN EL FORM VALID****')
        # opcion 1 de crear el modelo con .save()
        departamento = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortname']
        )
        departamento.save()
        # opcion 2 de crear el modelo con .create(), ya no necesita save
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            job='1',
            departamento=departamento
        )
        return super(NewDepartamentoView, self).form_valid(form)


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name="departamentos"
