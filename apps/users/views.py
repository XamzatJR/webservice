from .serializer import CustomUser, UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
