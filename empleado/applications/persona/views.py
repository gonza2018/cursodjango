from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    )
from django.views.generic.base import TemplateView
# models
from .models import Empleado
# Forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    ''' Vista que carga la página de inicio '''
    template_name = 'inicio.html'

# 1.- Listar todos los empleados de la empresa.
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        print('lista resultado', lista)
        return lista


class ListEmpleadosAdmin(ListView):
    template_name = 'persona/list_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


# 2.- Listar todos los empleados que pertenecen a un area de la empresa.
class ListByAreaEmpleado(ListView):
    '''Lista empleados de un Area'''
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        # El código que yo quiera
        area = self.kwargs['shor_name']
        lista = Empleado.objects.filter(
            departamento__shor_name= area
        )
        return lista

# 3.- Listar empleados por trabajo.
class ListByJob(ListView):
    '''Lista empleados por trabajo'''
    template_name = 'persona/list_by_job.html'

    def get_queryset(self):
        # El código que yo quiera
        jobs = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            job = jobs
        )
        return lista

# 4.- Listar los empleados por palabra clave.
class ListEmpleadosByKword(ListView):
    '''Lista de empleados por palabra clave'''
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('****************************')
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        print('lista resultado', lista)
        return lista

# 5.- Listar habilidades de un empleado.


class ListHabilidadesEmpleado(ListView):
    '''Lista de habilidades de un empleado'''
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        print('****************************')
        empleado = Empleado.objects.get(id = 6)

        print(empleado.habilidades.all())
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # toot un proceso
        context['titulo'] = 'Empleado del mes'

        return context

class SuccessView(TemplateView):
    template_name = "persona/success.html"

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')
    
    def form_valid(self, form):
        #Lógica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]

    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('************* METODO POST ****************')
        print('==========================================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        #Lógica del proceso
        print('************* FORM VALID  ****************')
        print('******************************************')
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')





