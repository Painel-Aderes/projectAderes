from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from .models import Artesoes
from .serializers import ArtesoesSerializer

class ArtesoesViewSet(viewsets.ModelViewSet):
  queryset = Artesoes.objects.all()
  serializer_class = ArtesoesSerializer
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
