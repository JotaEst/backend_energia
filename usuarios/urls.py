from django.urls import path
from usuarios.views import listar_usuarios, crear_usuarios, actualizar_usuario, eliminar_usuarios

urlpatterns = [
    path('listar/', listar_usuarios),
    path('crear/', crear_usuarios),
    path('actualizar/<int:id_usuario>/', actualizar_usuario),
    path('eliminar/<int:id_usuario>/', eliminar_usuarios)
]
