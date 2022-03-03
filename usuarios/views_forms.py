from usuarios.forms import *
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from datetime import date, datetime, timedelta, timezone


class UsuariosView(View):
    def get(self, request):
        print(request.session['usuario']['id'])
        print(f'soy el usuario {request.user}')

        mensajes = Mensaje.objects.all()
        comentarios = Comentario.objects.all()
        contexto = {
            'formModel': MensajeForm(),
            'formModel_comentario': ComentarioForm(),
            'mensajes': mensajes.order_by("-created_at"),
            'comentarios': comentarios.order_by("-created_at"),
        }
        return render(request, 'usuarios/muro.html', contexto)

    def post(self, request):
        if MensajeForm(request.POST):
            form = MensajeForm(request.POST)
            this_Usuario_inline = Usuario.objects.get(
                id=request.session['usuario']['id'])
            if form.is_valid():
                mensaje_recibido = form.save(commit=False)
                mensaje_recibido.usuario = this_Usuario_inline
                mensaje_recibido.save()
                messages.success(request, 'Mensaje Posteado con exito')
                return redirect(reverse('usuarios:muro'))


class AgregarComentario(View):
    def post(self, request, pk):
        print(pk)
        form = ComentarioForm(request.POST)
        print(request.POST)
        this_Usuario_inline = Usuario.objects.get(
            id=request.session['usuario']['id'])
        print(this_Usuario_inline.nombre)
        this_mensaje = Mensaje.objects.get(
            id=pk)
        print(this_mensaje.mensaje)
        if form.is_valid():
            comentario_recibido = form.save(commit=False)
            comentario_recibido.mensaje = this_mensaje
            comentario_recibido.usuario = this_Usuario_inline
            comentario_recibido.save()
            messages.success(request, 'Comentario Posteado con exito')
            return redirect(reverse('usuarios:muro'))
        else:
            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'usuarios/formulario_form.html', {'formModel': form})


class EliminarComentario(View):
    def get(self, request, pkcomment):
        print(f'id de comentario: {pkcomment}')
        # print(Comentario.objects.get(id=pkcomment).created_at)
        fecha_comentario = Comentario.objects.get(id=pkcomment).created_at
        fecha_actual = datetime.now(timezone.utc)
        diferencia_minutos = (
            ((fecha_actual-fecha_comentario).total_seconds())/60)
        print(diferencia_minutos)
        if diferencia_minutos <= 30:
            comentario_del = Comentario.objects.get(id=pkcomment)
            comentario_del.delete()
            messages.success(request, 'Comentario Eliminado con exito')
            return redirect(reverse('usuarios:muro'))
        else:
            messages.error(
                request, 'No puedes borrar tu comentario. Han pasado más de 30 minutos')
            return redirect(reverse('usuarios:muro'))

# class EliminarPost(View):
#     def get(self, request, pkpost):
#         print(f'id de mensaje: {pkpost}')
#         mensaje_del = Mensaje.objects.get(id=pkpost)
#         mensaje_del.delete()
#         messages.success(request, 'Mensaje Eliminado con exito')
#         return redirect(reverse('usuarios:muro'))
