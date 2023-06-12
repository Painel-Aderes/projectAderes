from rest_framework import serializers
from .models import *

# Apenas vinculação dos bancos diretamente a eles sem user de FK;
class ArtesoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artesoes
        fields = '__all__'
          
class JuntaComercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = JuntaComercial
        fields = '__all__'

class MicrocreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microcredito
        fields = '__all__'

class Municipio(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

# class seger(serializers.ModelSerializer):
#     class Meta:
#         model = seger
#         fields = '__all__'
        
