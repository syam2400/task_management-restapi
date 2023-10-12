from django.shortcuts import render
from task.models import Task
from task.serializer import TaskSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AllTask(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DueTask(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Task.objects.filter(completed=False)
    serializer_class = TaskSerializer


class CompTask(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Task.objects.filter(completed=True)
    serializer_class = TaskSerializer
