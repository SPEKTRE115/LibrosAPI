from rest_framework import serializers
from .models import Genero
from .models import Libro
from .models import Autor
from .models import Editorial

######################################################
# Serializadores de la API                           #
######################################################

#Serializador para los objetos de tipo Genero
class GeneroSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genero

#Serializador para los objetos de tipo Autor
class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Autor

#Serializador para los objetos de tipo Editorial
class EditorialSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Editorial

#Serializador para los objetos de tipo Libro
class LibroSerializer(serializers.ModelSerializer):
    generos = GeneroSerializer(read_only=True, many=True)
    autores = AutorSerializer(read_only=True, many=True)
    #editorial = EditorialSerializer(read_only=True, many=True)

    class Meta:
        fields = '__all__'
        model = Libro