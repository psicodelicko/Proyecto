from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, ParseError
from django.views.decorators.csrf import csrf_exempt
#from yaml import serialize
from core.models import Producto
from .serializers import ProductoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



@csrf_exempt
@api_view(['GET', 'POST'])
##@permission_classes((IsAuthenticated,))
def lista_Producto(request):
    """
    LISTA DE TODOS LOS Productos 
    """
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':        
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes((IsAuthenticated,))
def detalle_Producto(request, id):
    """
    GET, UPDATE O DELETE DE UN VEHICULO EN PARTICULAR
    """
    try:
        producto = Producto.objects.get(idProducto=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(Producto)
        return Response(serializer.data)
    if request.method == 'PUT':        
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(Producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)