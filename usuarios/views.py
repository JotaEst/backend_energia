import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UsuarioModel
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

# -------------------- CRUD Usuarios --------------------
def listar_usuarios(request):
    usurios = list(UsuarioModel.objects.values())
    return JsonResponse({'usuarios': usurios}, safe=False)

@csrf_exempt
def crear_usuarios(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            usuario = UsuarioModel.objects.create(usuario=data["usuario"])
            return JsonResponse({'mensaje': 'Usuario creado', 'id_usuario':usuario.id_usuario})
        except:
            return JsonResponse({'error':'No se ha podido crear el usuario'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def actualizar_usuario(request, id_usuario):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            usuario = UsuarioModel.objects.get(id_usuario=id_usuario)
            usuario.usuario = data["usuario"]
            usuario.save()
            return JsonResponse({'mensaje': 'Usuario actualizado'})
        except ObjectDoesNotExist:
            return JsonResponse({'error':'Usuario no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def eliminar_usuarios(request, id_usuario):
    if request.method == "DELETE":
        try:
            usuario = UsuarioModel.objects.get(id_usuario=id_usuario)
            usuario.delete()
            return JsonResponse({'mensaje': 'Usuario eliminado'})
        except ObjectDoesNotExist:
            return JsonResponse({'error':'Usuario no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)