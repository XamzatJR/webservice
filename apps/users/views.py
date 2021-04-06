from django.contrib.auth import views
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from rest_framework import generics, permissions
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

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

    def form_valid(self, form):
        user = form.save(commit=False)
        if user.is_expert is True:
            user.is_active = False
            user.save()
            return HttpResponseRedirect(reverse_lazy("login_expert_url"))
        user.save()
        return HttpResponseRedirect(reverse_lazy("login_url"))


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


class ExpertLoginView(View):
    template_name = "users/login_expert.html"

    def get(self, request):
        return render(request, self.template_name)


class Experts(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            users = CustomUser.objects.filter(is_expert=True, is_active=False)
            return render(
                request, "users/experts_output.html", context={"experts": users}
            )
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class ActiveExpert(View):
    def get(self, request, pk):
        if request.user.is_staff:
            user = CustomUser.objects.filter(pk=pk).first()
            user.is_active = True
            user.save()
        return HttpResponseRedirect(reverse_lazy("experts"))
