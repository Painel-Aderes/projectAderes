from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from .models import Artesoes, JuntaComercial, Microcredito
from .serializers import ArtesoesSerializer, JuntaComercialSerializer, MicrocreditoSerializer


class ArtesoesViewSet(viewsets.ModelViewSet):
  queryset = Artesoes.objects.all()
  serializer_class = ArtesoesSerializer
#   permission_classes = [permissions.IsAuthenticated]

class JunataComercialViewSet(viewsets.ModelViewSet):
  queryset = JuntaComercial.objects.all()
  serializer_class = JuntaComercialSerializer
  
class MicroCreditoViewSet(viewsets.ModelViewSet):
  queryset = Microcredito.objects.all()
  serializer_class = MicrocreditoSerializer