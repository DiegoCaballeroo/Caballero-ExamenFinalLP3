from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Caballero_Persona

# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'index.html')

def personas(request):
    return render(request, 'personas.html')

def agregar_persona(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        sexo = request.POST['sexo'] == 'True'  # Convertir a booleano

        persona = Caballero_Persona(
            nombre=nombre,
            apellidos=apellidos,
            sexo=sexo
        )
        persona.save()
        messages.success(request, f'Se agregó correctamente a la persona {persona.nombre} {persona.apellidos}')
        return redirect('personas') 

    return render(request, 'agregar_persona.html')

def personas(request):
    persona = Caballero_Persona.objects.all()
    return render(request, 'personas.html', {'persona': persona})

def eliminar_persona(request, id):
    persona = get_object_or_404(Caballero_Persona, id=id)
    persona.delete()
    messages.success(request, f'Se eliminó correctamente a la persona {persona.nombre}')
    return redirect('personas')

