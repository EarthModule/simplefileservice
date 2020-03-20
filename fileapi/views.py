from django.shortcuts import render
from rest_framework import viewsets
from .models import FileModel
from .serializers import FileModelSerializer
# Create your views here.
class FileModelViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileModelSerializer