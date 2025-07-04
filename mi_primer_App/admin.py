from django.contrib import admin

# Register your models here.
from .models import Curso, Estudiante, Entregable

register_models = [Curso, Estudiante, Entregable]

admin.site.register(register_models)
