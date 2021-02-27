from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token

schema_view = get_schema_view(
    openapi.Info(title="Snippets API", default_version="v1",),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(
        r"^docs(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        r"^docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("api/", include("rest_framework.urls")),
    path("api/", include("apps.users.urls")),
    url(r"^api-token-auth/", obtain_jwt_token),
]

if settings.DEBUG:
    urlpatterns += [path("admin/", admin.site.urls)]
