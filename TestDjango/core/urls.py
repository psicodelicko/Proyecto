from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.Carrito import Carrito
from rest_framework import routers
#from TestDjango.core.models import Producto
from .views import Arbusto, ProductoViewset, agregar_producto, eliminar_producto, registro,home, Contacto,\
    Categoria1, F_Crear_Cuenta,form_mod_usuario,Nosotros,HistoricoCompra,index_home,InicioSesion1,\
    limpiar_carrito,listado_producto, Paypal,PerfilProducto,Producto1,Seguimiento,Tierra,\
    Macetero,index_homeOG, form_usuario,restar_producto, form_producto, Carrito,\
    form_mod_producto,form_borrar_producto , listado_usuario, form_borrar_usuario, PrecioCripto
# ,NavBar

router = routers.DefaultRouter()
router.register ('producto', ProductoViewset)


urlpatterns = [
    path('home1',home , name="Home"),
    path('', index_home, name="index_home"),
    path('Arbusto/', Arbusto, name="Arbusto"),
    path('home/',index_homeOG , name="home"),
    path('Contacto/', Contacto, name="Contacto"),
    path('Categoria1/', Categoria1, name="Categoria1"),
    path('F_Crear_Cuenta/', F_Crear_Cuenta, name="F_Crear_Cuenta"),
    path('form_mod_usuario/<id>', form_mod_usuario, name="form_mod_usuario"),
    path('form_usuario/', form_usuario, name="form_usuario"),
    path('form_producto/', form_producto, name="form_producto"),
    path('login',Carrito),
    path('HistoricoCompra/', HistoricoCompra, name="HistoricoCompra"),
    #path('Home/', index_home, name="Home"),
    path('InicioSesion1/', InicioSesion1, name="InicioSesion1"),
    path('listado_producto/', listado_producto, name="listado_producto"),
    path('listado_usuario/', listado_usuario, name="listado_usuario"),
    path('registro',registro, name="registro"),
    path('Macetero/', Macetero, name="Macetero"),
    path('Nosotros/', Nosotros, name="Nosotros"),
    path('Paypal/', Paypal, name="Paypal"),
    path('PerfilProducto/<id>', PerfilProducto, name="PerfilProducto"),
    path('Producto/', Producto1, name="Producto"),
    path('Seguimiento/', Seguimiento, name="Seguimiento"),
    path('Tierra/', Tierra, name="Tierra"),
    #path('Nav/', NavBar, name="Nav"),
    path('agregar_producto/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="del"),
    path('restar/<int:producto_id>/', restar_producto, name="sub"),
    path('limpiar/', limpiar_carrito, name="cls"),
    path('form_mod_producto/<id>/', form_mod_producto, name="form_mod_producto"),
    path('form_borrar_producto/<id>/',form_borrar_producto, name="form_borrar_producto"),
    path('form_borrar_usuario/<id>/',form_borrar_usuario, name="form_borrar_usuario"),
    path('api/', include(router.urls)),
    path('PrecioCripto/', PrecioCripto, name="PrecioCripto"),

]


urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
##urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
