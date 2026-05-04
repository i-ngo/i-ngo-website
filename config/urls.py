from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from health_check.views import HealthCheckView
from landing.views import page_not_found

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", include("django_components.urls")),
    path("", include("landing.urls")),
    path("feed/", include("landing.urls")),
    path("projects/", include("landing.urls")),
    path("contact/", include("landing.urls")),
    path(
        "health/",
        HealthCheckView.as_view(
            checks=[
                "health_check.Database",
            ]
        ),
    ),
    re_path(r"^.*$", page_not_found),
]

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
