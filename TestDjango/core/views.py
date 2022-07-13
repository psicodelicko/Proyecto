from ast import Try
from distutils.command import clean
from email import message
from itertools import product
from math import prod
from pyexpat.errors import messages
from re import U
from sqlite3 import DateFromTicks
from tokenize import Triple
from urllib import request
from warnings import catch_warnings
from xml.dom.minidom import Document
from xml.parsers.expat import model
import django
from django.shortcuts import redirect, render
from core.forms import RegistrarProducto, RegistrarUsuario , CustomerUserCreationForm, ModificarUsuario, CrearCuentaAdmin
from django.contrib.auth import authenticate, login
from core.Carrito import Carrito
from django.contrib import messages
from django.contrib.auth.models import User 
from rest_framework import viewsets
from .serializers import ProductoSerializer
from .models import Producto, Usuario





class ProductoViewset(viewsets.ModelViewSet):
    #authentication_classes=[]
    #permission_classes=[]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()
        nombreProducto = self.request.GET.get('nombreProducto')

        if nombreProducto:
            productos = productos.filter(nombreProducto__contains=nombreProducto)

        return productos     

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    
    datos = {
        'productos': productos,
        "nombre": "diego araya"
    }  
    return render(request, 'core/home.html', datos)


def Producto1(request):
    productos =Producto.objects.all()
    datos = {
        'productos':productos
    }
    return render(request, 'core/Producto1.html', datos)  

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.agregar_producto(producto)
    return redirect("Producto")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.eliminar(producto)
    return redirect("Producto")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.restar(producto)
    return redirect("Producto") 

def limpiar_carrito(request):
    carrito = Carrito(request)   
    carrito.limpiar()
    return redirect("Producto") 

def Arbusto(request):
    productos =Producto.objects.filter(categoria="arbusto")
    datos = {
        'productos':productos
    }
    return render(request, 'core/Arbusto.html',datos)

def Contacto(request):
    return render(request, 'core/Contacto.html')

def Categoria1(request):
    return render(request, 'core/Categoria1.html')

def F_Crear_Cuenta(request):

    return render(request, 'core/F_Crear_Cuenta.html')

def form_mod_usuario(request):
    return render(request, 'core/form_mod_usuario.html')

def form_borrar_producto(request,id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    productos =Producto.objects.all()
    messages.success(request,"Producto eliminado correctamente")
    
    datos = {
        'productos':productos
    }
    return render(request, 'core/listado_producto.html',datos)

def form_borrar_usuario(request,id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    usuarios =User.objects.all()
    messages.success(request,"Usuario eliminado correctamente")
    datos = {
        'usuarios':usuarios
    }
    return render(request, 'core/listado_usuario.html',datos)

def HistoricoCompra(request):
    return render(request, 'core/HistoricoCompra.html')

def index_home(request):
    productos =Producto.objects.filter(precioProducto__lte=12990)
    datos = {
        'productos':productos
    }
    return render(request, 'core/index_home.html',datos)    

def index_homeOG(request):
    return render(request, 'core/index_homeOG.html')    

def InicioSesion1(request):
    return render(request, 'core/InicioSesion1.html')             

def listado_producto(request):
    productos =Producto.objects.all()
    datos = {
        'productos':productos
    }
    return render(request, 'core/listado_producto.html',datos) 

def listado_usuario(request):
    usuarios =User.objects.all()
    datos = {
        'usuarios': usuarios
    }
    return render(request, 'core/listado_usuario.html',datos)   

def Macetero(request):
    productos =Producto.objects.filter(categoria="macetero")
    datos = {
        'productos':productos
    }
    return render(request, 'core/Macetero.html',datos)    

def Nosotros(request):
    return render(request, 'core/Nosotros.html')                

def Paypal(request):
    return render(request, 'core/Paypal.html')   

def PerfilProducto(request,id):
    datos ={
        'producto' : Producto.objects.get(idProducto= id)
    }
    
    return render(request, 'core/PerfilProducto.html',datos)      

def Seguimiento(request):
    return render(request, 'core/Seguimiento.html')      

def Tierra(request):
    productos =Producto.objects.filter(categoria="tierra de hojas")
    datos = {
        'productos':productos
    }
    return render(request, 'core/Tierra.html',datos)     

def form_usuario(request):
    datos = {
        'form': CrearCuentaAdmin()
    }

    if request.method == 'POST':
        formmulario = CrearCuentaAdmin(request.POST)
        if formmulario.is_valid:
            formmulario.save()
            messages.success(request,"Cuenta administrdora registrada correctamente")
            datos['mensaje'] = "Guardados Correctamente"
            return redirect(to="listado_usuario")

            

    return render(request, 'core/form_usuario.html',datos)          

def form_producto(request):
    datos = {
        'form': RegistrarProducto()
    }
    if request.method == 'POST':

        formmulario = RegistrarProducto(request.POST , request.FILES)

        if formmulario.is_valid():
            formmulario.save()
            messages.success(request,"Producto registrado correctamente")
            datos['mensaje'] = "Guardados Correctamente"
    return render(request, 'core/form_producto.html',datos)                          


def F_Crear_Cuenta(request):
    datos = {
        'form': RegistrarUsuario()
    }

    if request.method == 'POST':

        formmulario = RegistrarUsuario(request.POST)

        if formmulario.is_valid:
            formmulario.save()
            datos['mensaje'] = "Guardados Correctamente"

    return render(request, 'core/F_Crear_Cuenta.html',datos)

def form_mod_usuario(request,id):
    usuario =User.objects.get(id = id)
    datos={
        'form': ModificarUsuario(instance=usuario)
    }
    if request.method == 'POST':
        formulario = ModificarUsuario(data=request.POST, instance= usuario)
        if formulario.is_valid:
            formulario.save()
            messages.success(request,"Usuario modificado correctamente")
            datos={
                'form': ModificarUsuario(instance=usuario),
                'mensaje' : "Usuario Modificado corrctamente"
                }

    return render(request, 'core/form_mod_usuario.html',datos)

def form_mod_producto(request,id):
    producto =Producto.objects.get(idProducto = id)
    datos={
        'form': RegistrarProducto(instance=producto)
    }
    if request.method == 'POST':
        formulario = RegistrarProducto(data=request.POST,files=request.FILES, instance= producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto modificado correctamente")
            datos={
                'form': RegistrarProducto(instance=producto),
                'mensaje' : "Modificado corretamente"
                }

    return render(request, 'core/form_mod_producto.html',datos)


def registro (request):
    data ={
        'form':CustomerUserCreationForm
    }
    if request.method =='POST':
        formulario = CustomerUserCreationForm(data= request.POST)
        if formulario.is_valid:
            formulario.save()
            messages.success(request,"Te has registrado correctamente")
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect(to="index_home")
        data["form"] = formulario
    return render(request, 'registration/registro.html',data)

def PrecioCripto(request):
    return render(request, 'core/PrecioCripto.html')

#def NavBar(request):
 #   return render(request, 'core/NavBar.html')  
     