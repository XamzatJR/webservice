from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import UserCreate

urlpatterns = [
    path("auth/register/", UserCreate.as_view()),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", views.LoginView.as_view(), name="login_url"),
    path("logout/", views.LogoutView.as_view(), name="logout_url"),
    path("registration/", views.RegistrationView.as_view(), name="registration_url"),
    path(
        "password_reset/", views.PasswordResetView.as_view(), name="password_reset_url"
    ),
    path(
        "password_reset_done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done_url",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm_url",
    ),
    path(
        "password_reset_complete/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete_url",
    ),
]
