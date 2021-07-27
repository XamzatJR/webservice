from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, InviteCode


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "username", "is_expert", "is_active")
    list_filter = ("is_expert", "is_active")
    fieldsets = (
        (
            None,
            {"fields": ("email", "username", "last_name", "first_name", "password", "photo")},
        ),
        (
            "Права доступа",
            {"fields": ("is_superuser", "is_staff", "is_expert", "is_active")},
        ),
        ("Важные даты", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "last_name",
                    "first_name",
                    "password1",
                    "password2",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(InviteCode)
