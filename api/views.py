from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Artesoes, JuntaComercial, Microcredito, Municipio
from .serializers import ArtesoesSerializer, JuntaComercialSerializer, MicrocreditoSerializer, MunicipioSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User


@api_view(['GET'])
def getArtesoes(request):
    artesoes = Artesoes.objects.all()
    serializerArtesoes = ArtesoesSerializer(artesoes, many=True)
    return Response(serializerArtesoes.data)

@api_view(['GET', 'POST'])
def GetPostArtesoes(request):
    """
    List all persons, or create a new person.
    """
    if request.method == 'GET':
        artesoes = Artesoes.objects.all()
        serializerArtesoes = ArtesoesSerializer(artesoes, many=True)
        return Response(serializerArtesoes.data)

    elif request.method == 'POST':
        serializerArtesoes = ArtesoesSerializer(data=request.data)
        if serializerArtesoes.is_valid():
            serializerArtesoes.save()
            return Response(serializerArtesoes.data, status=status.HTTP_201_CREATED)
        return Response(serializerArtesoes.errors, status=status.HTTP_400_BAD_REQUEST)


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
        serializerArtesoes = ArtesoesSerializer(artesoes)
        return Response(serializerArtesoes.data)

    elif request.method == 'PUT':
        serializerArtesoes = ArtesoesSerializer(artesoes, data=request.data)
        if serializerArtesoes.is_valid():
            serializerArtesoes.save()
            return Response(serializerArtesoes.data)
        return Response(serializerArtesoes.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artesoes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
##JUNTA COMERCIAL
@api_view(['GET'])
def getJuntacomercial(request):
    juntacomercial = JuntaComercial.objects.all()
    serializer = JuntaComercialSerializer(juntacomercial, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def getPostJuntacomercial(request):
    if request.method == 'GET':
        juntacomercial = JuntaComercial.objects.all()
        serializer = JuntaComercialSerializer(juntacomercial, many=True)

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
        serializer = MicrocreditoSerializer(juntacomercial)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MicrocreditoSerializer(juntacomercial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        juntacomercial.delete()
        return Response(status.HTTP_204_NO_CONTENT)
##MICROCREDITO
@api_view(['GET'])
def getMicroCredito(request):
    microcredito = Microcredito.objects.all()
    serializer = MicrocreditoSerializer(microcredito, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def getPostMicroCredito(request):
    if request.method == 'GET':
        microcredito = Microcredito.objects.all()
        serializer = Microcredito(microcredito, many=True)

    elif request.method == 'POST':
        serializer = MicrocreditoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def GetPutDellMunicipio(request, pk):
    try:
        microcredito = Municipio.objects.get(pk=pk)
    except Microcredito.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MicrocreditoSerializer(microcredito)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MicrocreditoSerializer(microcredito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        microcredito.delete()
        return Response(status.HTTP_204_NO_CONTENT)
##MUNICIPIO
@api_view(['GET'])
def getMunicipio(request):
    municipio = Municipio.objects.all()
    serializer = MunicipioSerializer(municipio, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def getPostMunicipio(request):
    if request.method == 'GET':
        municipio = Municipio.objects.all()
        serializer = Municipio(municipio, many=True)

    elif request.method == 'POST':
        serializer = MunicipioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def GetPutDellMuni(request, pk):
    try:
        municipio = Municipio.objects.get(pk=pk)
    except Municipio.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MunicipioSerializer(municipio)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MunicipioSerializer(municipio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        municipio.delete()
        return Response(status.HTTP_204_NO_CONTENT)
