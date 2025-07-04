from django.urls import path
from .views import inicio, crear_curso, crear_estudiante, buscar_cursos, cursos, crear_entregable

urlpatterns = [
    path('', inicio, name='inicio'),  
    #path('holamundo/', saludo),
    #path('hola-mundo-template/', saludo_con_template),
    #path('crear-familiar/<str:nombre>', crear_familiar),
    path('crear-curso/', crear_curso, name='crear-curso'),
    path('crear-estudiante/', crear_estudiante, name='crear-estudiante'),
    path('cursos/', cursos, name='cursos'),
    path('buscar-cursos/', buscar_cursos, name='buscar-cursos'),
    path('crear-entregable/', crear_entregable, name='crear-entregable'),
]


