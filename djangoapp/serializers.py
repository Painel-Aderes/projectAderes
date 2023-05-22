from rest_framework import serializers
from .models import *

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Artesoes
#         fields = '__all__'

class ArtesoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artesoes
        fields = '__all__'