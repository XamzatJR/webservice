from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserCreate

urlpatterns = [
    path("register/", UserCreate.as_view()),
    path("register/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
