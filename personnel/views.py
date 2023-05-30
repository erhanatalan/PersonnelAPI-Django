from django.shortcuts import render
from .serializers import DepartmentSerializer, PersonnelSerializer, DepartmentPersonnelSerializer
from .models import Department, Personnel
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)


class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

     


class PersonnelListCreateView(ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer


class PersonnelRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

class DepartmentPersonnelView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentPersonnelSerializer



