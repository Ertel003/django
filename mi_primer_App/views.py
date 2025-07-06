from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Entregable
from .forms import CursoForm, EstudianteForm, EntregableForm

# Create your views here.

#from django.http import HttpResponse

def inicio(request):
    return render(request, 'mi_primer_App/inicio.html')

#def saludo(request):
#    return HttpResponse("¡Hola, mundo!")

#def saludo_con_template(request):
#    return render(request, 'mi_primer_App/saludo.html')

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_curso = Curso(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                duracion_semanas=form.cleaned_data['duracion_semanas'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                activo=form.cleaned_data['activo']
            )
            nuevo_curso.save()
            return redirect('cursos')
    else:
        form = CursoForm()
        return render(request, 'mi_primer_app/crear_curso.html', {'form': form})


def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_curso = Estudiante(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                edad=form.cleaned_data['edad'],
                fecha_inscripcion=form.cleaned_data['fecha_inscripcion']
            )
            nuevo_curso.save()
            return redirect('inicio')
    else:
        form = EstudianteForm()
        return render(request, 'mi_primer_app/crear_estudiante.html', {'form': form})


def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos})


def buscar_cursos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos, 'nombre': nombre})

def crear_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el entregable
            nuevo_entregable = Entregable(
                nombre = form.cleaned_data['nombre'],
                fecha_entrega = form.cleaned_data['fecha_entrega'],
                entregado = form.cleaned_data['entregado'],
                estudiante = form.cleaned_data['estudiante']
            )
            nuevo_entregable.save()
            return redirect('inicio')
    else:
        form = EntregableForm()
        return render(request, 'mi_primer_app/crear_entregable.html', {'form': form})
    