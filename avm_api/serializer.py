"""Un serializador nos permite convertir objetos de python a json y viceversa, es similar a un formuladrio donde
 defines los campos a ingresar"""

from rest_framework import serializers

class AvmApiSerializer(serializers.Serializer):
    """serializar campos para la APIView"""

    address = serializers.CharField(max_length=50)