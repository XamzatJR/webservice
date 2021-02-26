from django.urls import path, include

from .views import *

urlpatterns = [path("account/register", UserCreate.as_view())]
