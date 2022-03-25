from re import template
from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)
#import models
from .models import Prueba
#import form
from .forms import PruebaForm

# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen_foundation.html'


class PruebaListView(ListView):
    #model = Prueba
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0', '1', '10', '20', '30']

class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = "lista"


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    # fields = ['titulo', 'subtitulo', 'cantidad'] este fields se quita ed aqui ya que usamos forms.py
    form_class = PruebaForm
    success_url = '/home/'

