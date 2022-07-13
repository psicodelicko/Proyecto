from django.urls import path
from rest_producto.views import lista_Producto, detalle_Producto
from rest_producto import views
#from rest_producto.viewslogin import login

urlpatterns = [
    path('lista_Producto', lista_Producto, name="lista_Producto"),
    #path('login', login, name="login"),
    path('detalle_Producto', detalle_Producto, name="detalle_Producto"),
]