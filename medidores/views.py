import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from usuarios.models import UsuarioModel
from .models import MedidorModel
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

# -------------------- CRUD medidores --------------------
def listar_medidores(request):
    medidores = list(MedidorModel.objects.values())
    return JsonResponse({'medidores': medidores}, safe=False)

@csrf_exempt
def crear_medidor(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            try:
                id_usuario = UsuarioModel.objects.get(id_usuario=data["id_usuario"])
            except UsuarioModel.DoesNotExist:
                return JsonResponse({'mensaje': 'No se ha encontrado el usuario'}, status=404)

            ciudad = data["ciudad"]
            response = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={ciudad}&country=CO&count=1')
            localizacion = response.json()

            pais = localizacion['results'][0]['country_code']
            if pais != 'CO':
                return JsonResponse({'error':'La ciudad ingresada no es de Colombia'}, status=404)
            
            latitud = localizacion['results'][0]['latitude'] if 'results' in localizacion else None
            longitud = localizacion['results'][0]['longitude'] if 'results' in localizacion else None
                      
            medidor = MedidorModel.objects.create(
                id_usuario=id_usuario,
                ciudad=ciudad,
                latitud=latitud,longitud=longitud)

            return JsonResponse({'mensaje': 'Medidor creado', 'numero de serie':medidor.numero_serie})
        except:
            return JsonResponse({'error':'No se ha podido crear el medidor'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def actualizar_medidor(request, numero_serie):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            medidor = MedidorModel.objects.get(numero_serie=numero_serie)

            try:
                id_usuario = UsuarioModel.objects.get(id_usuario=data["id_usuario"])
            except UsuarioModel.DoesNotExist:
                return JsonResponse({'mensaje': 'No se ha encontrado el usuario'}, status=404)

            medidor.id_usuario_id = id_usuario
            medidor.save()
            return JsonResponse({'mensaje': 'Medidor actualizado'})
        except ObjectDoesNotExist:
            return JsonResponse({'error':'Medidor o usuario no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def eliminar_medidor(request, numero_serie):
    if request.method == "DELETE":
        try:
            medidor = MedidorModel.objects.get(numero_serie=numero_serie)
            medidor.delete()
            return JsonResponse({'mensaje': 'Medidor eliminado'})
        except ObjectDoesNotExist:
            return JsonResponse({'error':'Medidor no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)