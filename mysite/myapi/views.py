from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CreatorSerializer
from .models import Creator

# Create your views here.


class CreaterViewSet(viewsets.ModelViewSet):
    queryset = Creator.objects.all().order_by('name')
    serializer_class = CreatorSerializer
