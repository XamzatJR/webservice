from django.contrib import admin
from django.urls import path, include
from users.models import CustomUser

from rest_framework import routers, serializers, viewsets


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("rest_framework.urls")),
    path("", include("users.urls")),
]
