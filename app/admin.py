from django.contrib import admin
from app.models import Proyectos

class Proyectosadmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')   

admin.site.register(Proyectos, Proyectosadmin)

