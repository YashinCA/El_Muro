from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from usuarios.models import Usuario
from django.contrib import messages


def list_usuarios(request):
    # para ver que trae el request
    # print(request.__dict__)
    contexto = {
        'usuarios': Usuario.objects.all(),
    }

    return render(request, 'usuarios/lista.html', contexto)


def add_usuarios(request):
    if request.method == 'GET':
        return render(request, 'usuarios/formulario.html')

    if request.method == 'POST':
        print(request.POST)
        error = Usuario.objects.basic_validator(request.POST)

        if len(error) > 0:
            request.session['nombre'] = request.POST['nombre']
            request.session['apellido'] = request.POST['apellido']
            request.session['username'] = request.POST['username']
            request.session['email'] = request.POST['email']
            for valor in error.values():
                messages.error(request, valor)

            return render(request, 'usuarios/formulario.html')

        else:
            Usuario.objects.create(
                nombre=request.POST['nombre'],
                apellido=request.POST['apellido'],
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
            )
            messages.success(request, "Usuario agregado exitosamente!")
            return redirect(reverse('usuarios:listado'))


def delete_usuarios(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'usuario': usuario,
        }
        return render(request, 'usuarios/delete.html', contexto)

    if request.method == 'POST':
        usuario.delete()

        return redirect(reverse('usuarios:listado'))


def delete_usuarios_api(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return JsonResponse({'success': True})
