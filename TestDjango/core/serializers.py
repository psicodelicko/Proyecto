from .models import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


    def validate_nombreProducto(self, value):
        existe = Producto.objects.filter(nombreProducto__iexact=value).exists()
        if existe:
            raise serializers.ValidationError("Este producto ya existe")
        return value    




        