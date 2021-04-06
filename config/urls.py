from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from .yasg import urlpatterns as yasg

urlpatterns = (
    [
        path("", include("apps.users.urls")),
        path("", include("rest_framework.urls")),
        path("", include("apps.projects.urls")),
    ]
    + yasg
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

if settings.DEBUG:
    urlpatterns += [path("admin/", admin.site.urls)]
