from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from .models import *
from .serializers import ArtesoesSerializer, JuntaComercialSerializer, MicrocreditoSerializer


class ArtesoesViewSet(viewsets.ModelViewSet):
  queryset = Artesoes.objects.all()
  serializer_class = ArtesoesSerializer
  permission_classes = [permissions.IsAuthenticated]


class JuntaComercialViewSet(viewsets.ModelViewSet):
  queryset = JuntaComercial.objects.all()
  serializer_class = JuntaComercialSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  
class MicrocreditoViewSet(viewsets.ModelViewSet):
  queryset = Microcredito.objects.all()
  serializer_class = MicrocreditoSerializer
  permission_classes = [permissions.IsAuthenticated]

# @api_view(['GET'])
# def getData(request):
#     users = Artesoes.objects.all()
#     serializer = ArtesoesSerializer(users, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getUser(request, pk):
#     users = Artesoes.objects.get(id=pk)
#     serializer = ArtesoesSerializer(users, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def addUser(request):
#     serializer = ArtesoesSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['PUT'])
# def updateUser(request, pk):
#     user = Artesoes.objects.get(id=pk)
#     serializer = ArtesoesSerializer(instance=user, data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['DELETE'])
# def deleteUser(request, pk):
#     user = Artesoes.objects.get(id=pk)
#     user.delete()
#     return Response('User successfully deleted!')