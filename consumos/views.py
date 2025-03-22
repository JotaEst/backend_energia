import json
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from medidores.models import MedidorModel
from .models import ConsumoModel
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def consultar_consumos(request,numero_serie):
    try:
        MedidorModel.objects.get(numero_serie=numero_serie)
    except MedidorModel.DoesNotExist:
        return JsonResponse({'mensaje': 'No se ha encontrado el medidor'}, status=404)

    consumos = list(ConsumoModel.objects.filter(numero_serie=numero_serie).values())
    
    if not consumos:
        return JsonResponse({'mensaje': 'No se han encontrado consumos en el medidor'}, status=404)
    
    return JsonResponse({'consumos': consumos, "numero_serie":numero_serie}, safe=False)

@csrf_exempt
def generar_consumos(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            numero_serie=data["numero_serie"]
            
            if not numero_serie:
                return JsonResponse({"error": "Falta el número de serie"}, status=400)

            try:
                medidor = MedidorModel.objects.get(numero_serie=numero_serie)
            except MedidorModel.DoesNotExist:
                return JsonResponse({"error": "Medidor no encontrado"}, status=404)

            consumo = ConsumoModel.objects.create(
                numero_serie_id=medidor.numero_serie,consumo_kwh=round(random.uniform(10,220),2))
            return JsonResponse({'mensaje': 'Se ha generado un consumo',
            "numero_serie":consumo.numero_serie_id,
            "consumo_kwh":consumo.consumo_kwh,
            "fecha":consumo.fecha_consumo.strftime("%Y-%m-%d %H:%M:%S")})
        except:
            return JsonResponse({'error':'No se ha podido generar el consumo'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
