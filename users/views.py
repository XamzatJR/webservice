from django.shortcuts import render
from .serializer import *
from rest_framework import *
from rest_framework.permissions import AllowAny, IsAdminUser


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
