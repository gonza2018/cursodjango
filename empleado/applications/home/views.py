from django.shortcuts import render
#
from django.views.generic import (
    TemplateView,
    ListView, 
    CreateView
)

# Import models
from .models import Prueba
from .forms import PruebaForm

# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumeFoundationView(TemplateView):
    template_name = 'home/resumen_foundation.html'

class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30']

class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'

class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = '/'



