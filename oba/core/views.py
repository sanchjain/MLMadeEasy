from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers

# Create your views here.
class FileList(generics.ListCreateAPIView):
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer