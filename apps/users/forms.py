from django import forms
from django.contrib.auth import forms as user_forms
from django.db.models.fields import BooleanField

from .models import CustomUser


class CustomUserCreationForm(user_forms.UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"


class CustomUserChangeForm(user_forms.UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"


class CustomUserLoginForm(user_forms.AuthenticationForm, forms.ModelForm):
    """Форма для авторизации"""

    class Meta:
        model = CustomUser
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].label = ""
        self.fields["username"].widget.attrs["placeholder"] = "Имя пользователя"
        self.fields["password"].widget.attrs["placeholder"] = "Пароль"


class CustomUserRegistrationForm(user_forms.UserCreationForm):
    """Форма для регистрации"""

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "last_name",
            "first_name",
            "email",
            "password1",
            "password2",
            "is_expert",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field], BooleanField):
                self.fields[field].widget.attrs["class"] = "form-control"
                continue
            self.fields[field].help_text = None
            self.fields[field].label = ""
        self.fields["username"].widget.attrs["placeholder"] = "Имя пользователя"
        self.fields["last_name"].widget.attrs["placeholder"] = "Фамилия"
        self.fields["first_name"].widget.attrs["placeholder"] = "Имя"
        self.fields["email"].widget.attrs["placeholder"] = "Электронная почта"
        self.fields["password1"].widget.attrs["placeholder"] = "Пароль"
        self.fields["password2"].widget.attrs["placeholder"] = "Подтверждение пароля"
        self.fields["is_expert"].label = "Зарегистрироваться как эксперт"
