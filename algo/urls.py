from django.contrib import admin
from django.urls import path
from django.urls import include
from acceso.utils.decoradores import login_requerido
from decorator_include import decorator_include

urlpatterns = [
    path('', decorator_include(login_requerido, include('app.urls'))),
    path('wall/', decorator_include(login_requerido, include('usuarios.urls'))),
    path('acceso/', include('acceso.urls')),
    path('admin/', admin.site.urls),
]
