from django.urls import path

from .views import UserCreate

urlpatterns = [path("user/register", UserCreate.as_view())]
