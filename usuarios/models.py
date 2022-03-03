from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    username = models.CharField(
        max_length=20, unique=True, verbose_name="Nombre de Usuario")
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=72)
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # mensajes=lista de mensajes hechas por el usuario
    # comentarios=lista que ha hecho el usuario


class Mensaje(models.Model):
    mensaje = models.TextField()
    usuario = models.ForeignKey(
        Usuario, related_name="mensajes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comentarios_mensaje=lista de cometarios en un mensaje

    def __str__(self):
        return self.mensaje


class Comentario(models.Model):
    comentario = models.TextField()
    usuario = models.ForeignKey(
        Usuario, related_name="comentarios_usuario", on_delete=models.CASCADE)
    mensaje = models.ForeignKey(
        Mensaje, related_name="comentarios_mensaje", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comentario
