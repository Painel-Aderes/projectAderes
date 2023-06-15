from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from .models import Artesoes, JuntaComercial
from .serializers import ArtesoesSerializer, JuntaComercialSerializer, MicrocreditoSerializer


class ArtesoesViewSet(viewsets.ModelViewSet):
  queryset = Artesoes.objects.all()
  serializer_class = ArtesoesSerializer
#   permission_classes = [permissions.IsAuthenticated]

