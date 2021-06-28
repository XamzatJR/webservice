from random import choices, randint
from string import ascii_letters, digits

from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import CreateView, View, ListView
from django.views.generic.edit import UpdateView

from .forms import CustomUserLoginForm, CustomUserRegistrationForm
from .models import InviteCode
from .serializer import CustomUser
from .utils import IsAdminMixin, UserAuthenticatedMixin
from .forms import UserChangeForm

# class UserCreate(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.AllowAny,)


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

    def get(self, request, *args: str, **kwargs):
        if code := request.GET.get("code"):
            if InviteCode.get_or_none(code=code):
                return super().get(request, *args, **kwargs)
        return HttpResponseRedirect(reverse("login_url"))

    def post(self, request, *args, **kwargs):
        if code := request.GET.get("code"):
            if code_model := InviteCode.get_or_none(code=code):
                code_model.delete()
                return super().post(request, *args, **kwargs)
        return HttpResponseRedirect(reverse("login_url"))

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
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


class ExpertLoginView(UserAuthenticatedMixin, views.LoginView):
    template_name = "users/login_expert.html"
    form_class = CustomUserLoginForm
    success_url = reverse_lazy("index_url")

    def get_success_url(self):
        return self.success_url


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


class CreateInviteCode(IsAdminMixin, ListView):
    model = InviteCode
    template_name = "users/createcode.html"
    context_object_name = "codes"


def create_code(request):
    if request.is_ajax():
        code = "".join(choices(ascii_letters + digits, k=randint(50, 99)))
        InviteCode.objects.create(code=code).save()
        return JsonResponse(
            {"link": f"{request.META['HTTP_HOST']}/registration?code={code}"}
        )

class UserUpdateView(LoginRequiredMixin, UpdateView):
    """ профиль """

    model = CustomUser
    template_name = "users/photo_update.html"
    form_class = UserChangeForm

    def get_success_url(self):
        return reverse_lazy("photo_update_url", kwargs={"pk": self.object.pk})