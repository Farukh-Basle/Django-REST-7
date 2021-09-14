
from django.shortcuts import render
from ModelViewSet_App.models import Employee
from ModelViewSet_App.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet

from ModelViewSet_App.pagination import UserPagination

class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer

    pagination_class = UserPagination



    