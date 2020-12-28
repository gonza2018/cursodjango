from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )

    # Creación de la columna full_name
    def full_name(self, obj):
        # Toda la operación que se necesite
        print(obj.first_name)
        return obj.first_name + " " + obj.last_name


    # Buscar por nombre
    search_fields = ('first_name',)

    # Filtrar por tipo de trabajo
    list_filter = ('departamento', 'job', 'habilidades', )

    #Filtro horizontal para muchos a muchos
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)

