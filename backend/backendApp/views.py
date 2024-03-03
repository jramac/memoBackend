from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Name, Score
from .serializers import NameSerializer, ScoreSerializer

@api_view(['GET'])
def nameList(request):
    names = Name.objects.all()
    serializer = NameSerializer(names, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def nameCreate(request):
    serializer = NameSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        nadimak = serializer.data
        nadimak = nadimak.get("nadimak",None)
        return Response(f"Igrac sa imenom {nadimak} vec postoji")

@api_view(['POST'])
def nameUpdate(request,pk):
    name = Name.objects.get(id=pk)
    serializer = NameSerializer(instance = name, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def nameDelete(request,pk):
    name = Name.objects.get(id=pk)
    name.delete()
    return Response(200)

@api_view(['GET'])
def scoreList(request):
    scores = Score.objects.all()
    serializer = ScoreSerializer(scores, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def scoreCreate(request):
    serializer = ScoreSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['POST'])
def scoreUpdate(request,pk):
    score = Score.objects.get(id=pk)
    #print(score)
    #print(request.data)
    serializer = ScoreSerializer(instance = score, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def scoreDelete(request,pk):
    score = Score.objects.get(id=pk)
    score.delete()
    return Response(200)