from django.urls import path
from . import views
from . import views_forms
from .views_forms import UsuariosView, AgregarComentario, EliminarComentario

app_name = 'usuarios'

# 8000/usuarios/

urlpatterns = [
    path('', UsuariosView.as_view(), name='muro'),
    path('<int:pk>', AgregarComentario.as_view(), name='comentario'),
    path('delc/<int:pkcomment>',
         EliminarComentario.as_view(), name='deletecomentario'),
    # path('delp/<int:pkpost>',
    #      EliminarComentario.as_view(), name='deletepost'),
]
