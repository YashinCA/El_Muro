from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse


def index(request):
    context = {
        'saludo': f'Hola'
    }
    return redirect(reverse('usuarios:muro'))


def second(request, name):
    return HttpResponse('Hola ' + name)


def redirigir(request):
    return redirect('/')
