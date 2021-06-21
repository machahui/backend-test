from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Empresa
from .serializers import EmpresaSerializer
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from faker import Faker

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content = {"message": "Welcome to the empresastore!"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def generate_registros_empresas(request):
    listEmpresas = []
    for i in range(20):
        fake = Faker()
        values = {'name':fake.name(),'address':fake.address()}
        Empresa.objects.create(
            name=values["name"],
            address=values["address"],
        )
        listEmpresas.append(values)
    return JsonResponse({'empresas': listEmpresas}, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def get_empresas(request):
    # user = request.user.id
    empresas = Empresa.objects.all()
    serializer = EmpresaSerializer(empresas, many=True)
    return JsonResponse({'empresas': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def add_empresa(request):
    payload = json.loads(request.body)
    # user = request.user
    try:
        empresa = Empresa.objects.create(
            name=payload["name"],
            vat=payload["vat"],
            address=payload["address"],
        )
        serializer = EmpresaSerializer(empresa)
        return JsonResponse({'empresas': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def update_empresa(request, empresa_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        empresa = Empresa.objects.filter(id=empresa_id)
        # returns 1 or 0
        empresa.update(**payload)
        serializer = EmpresaSerializer(empresa)
        return JsonResponse({'empresa': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def delete_empresa(request, empresa_id):
    try:
        empresa = Empresa.objects.get(id=empresa_id)
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)