from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Artesoes
from .serializers import ArtesoesSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User


@api_view(['GET'])
def getData(request):
    users = Artesoes.objects.all()
    serializer = ArtesoesSerializer(users, many=True)
    return Response(serializer.data)

#Funciona 
@api_view(['GET', 'POST'])
def addUser(request):
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
def GetPutDell(request, pk):
    """
    Retrieve, update or delete a person instance.
    """
    try:
        person = Artesoes.objects.get(pk=pk)
    except Artesoes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtesoesSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtesoesSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def GetPutDell2(request):
    """
    Retrieve, update or delete a person instance.
    """
    try:
        person = Artesoes.objects.get()
    except Artesoes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtesoesSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtesoesSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)