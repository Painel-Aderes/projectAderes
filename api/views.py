from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Artesoes, JuntaComercial
from .serializers import ArtesoesSerializer, JuntaComercialSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User


@api_view(['GET'])
def getArtesoes(request):
    users = Artesoes.objects.all()
    serializer = ArtesoesSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def GetPostArtesoes(request):
    """
    List all persons, or create a new person.
    """
    if request.method == 'GET':
        persons = Artesoes.objects.all()
        serializer = ArtesoesSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtesoesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def GetPutDellArtesoes(request, pk):
    """
    Retrieve, update or delete a person instance.
    """
    try:
        artesoes = Artesoes.objects.get(pk=pk)
    except Artesoes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtesoesSerializer(artesoes)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtesoesSerializer(artesoes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artesoes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def getJuntacomercial(request):
    juntacomercial = JuntaComercial.objects.all()
    serializer = JuntaComercialSerializer(juntacomercial, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def getPostJuntacomercial(request):
    if request.method == 'GET':
        juntacomerical = JuntaComercial.objects.all()
        serializer = JuntaComercialSerializer(juntacomerical, many=True)
        
    elif request.method == 'POST':
        serializer = JuntaComercialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def GetPutDeleteJuntacomercial(request, pk):
    try:
        juntacomercial = JuntaComercial.objects.get(pk=pk)
    except JuntaComercial.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JuntaComercialSerializer(juntacomercial)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = JuntaComercialSerializer(juntacomercial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        juntacomercial.delete()
        return Response(status.HTTP_204_NO_CONTENT)