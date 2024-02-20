from django.shortcuts import render
from rest_framework import viewsets
from .models import Name, Score
from .serializers import NameSerializer, ScoreSerializer


class NameViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
