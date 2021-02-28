from .serializer import CustomUser, UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import *
from .models import CustomUser

class UserCreate(ListCreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
