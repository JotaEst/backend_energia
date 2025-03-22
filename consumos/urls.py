from django.urls import path
from consumos.views import consultar_consumos, generar_consumos

urlpatterns = [
    path('consultar/<int:numero_serie>/', consultar_consumos),
    path('generar/', generar_consumos)
]
