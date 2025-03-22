from django.urls import path
from medidores.views import listar_medidores, crear_medidor, actualizar_medidor, eliminar_medidor

urlpatterns = [
    path('listar/', listar_medidores),
    path('crear/', crear_medidor),
    path('actualizar/<int:numero_serie>/', actualizar_medidor),
    path('eliminar/<int:numero_serie>/', eliminar_medidor)
]
