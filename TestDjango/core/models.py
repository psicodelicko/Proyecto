from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria
   

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='Id de producto')
    nombreProducto = models.CharField(max_length=50,verbose_name='Nombre del producto')
    descripcionProducto = models.CharField(max_length=50,verbose_name='Descripcion del producto')
    precioProducto = models.IntegerField(verbose_name='Precio del producto')
    imagen = models.ImageField ( upload_to= 'producto', null= True, default=None)
    categoria = models.CharField(max_length=50,verbose_name='categoria')


    def __str__(self):
        return self.nombreProducto

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name='Id de usuario')
    nombreUsuario = models.CharField(max_length=50,verbose_name='Nombre de usuario')
    nombres = models.CharField(max_length=50,verbose_name='Nombres')
    apellidos = models.CharField(max_length=50,verbose_name='apellidos')
    contrasena = models.CharField(max_length=50, verbose_name='contrasena')
    def __str__(self):
        return self.nombreUsuario
