from rest_framework import serializers
from getPrecioProductos.models import TableName

class tesTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableName
        fields = ('nombre', 'apellido')