from django.shortcuts import render
from rest_framework import viewsets
from .models import TodosSchema
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodosSchema.objects.all()
    serializer_class = TodoSerializer