from django.contrib.auth import views
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import generics, permissions

from .forms import CustomUserLoginForm, CustomUserRegistrationForm
from .serializer import CustomUser, UserSerializer
from .utils import UserAuthenticatedMixin


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class LoginView(UserAuthenticatedMixin, views.LoginView):
    template_name = "users/login.html"
    form_class = CustomUserLoginForm
    success_url = reverse_lazy("index_url")

    def get_success_url(self):
        return self.success_url


class RegistrationView(CreateView):
    model = CustomUser
    template_name = "users/registration.html"
    form_class = CustomUserRegistrationForm
    success_url = reverse_lazy("login_url")


class LogoutView(views.LogoutView):
    next_page = reverse_lazy("login_url")


class PasswordResetView(views.PasswordResetView):
    template_name = "users/password_reset.html"
    success_url = reverse_lazy("password_reset_done_url")
    email_template_name = "users/password_reset_email.html"


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = "users/password_reset_done.html"


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = "users/password_reset_confirm.html"
    success_url = reverse_lazy("password_reset_complete_url")


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = "users/password_reset_complete.html"
