from .models import ToDo
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ToDoSerializer

# Create your views here.
class ToDoView(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

