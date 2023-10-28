import os
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/v1/admin/", include(("apps.api.urls.admin", "api"))),
    path("api/v1/front/", include(("apps.api.urls.front", "api"))),
]

if os.environ.get("DJANGO_SETTINGS_MODULE") == "config.settings.production":
    urlpatterns += [
        path("dfjeuhhdhsgdthahdhdhfkdklleewooiaujsjsau/", admin.site.urls),
    ]
else:
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

    urlpatterns += [
        path("admin/", admin.site.urls),
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "api/swagger/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
    ]
