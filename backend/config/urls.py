import os
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/v1/admin/", include(("apps.api.urls.admin", "api_admin"))),
    path("api/v1/front/", include(("apps.api.urls.front", "api_front"))),
]

if os.environ.get("DJANGO_SETTINGS_MODULE") == "config.settings.production":
    urlpatterns += [
        path("dfjeuhhdhsgdthahdhdhfkdklleewooiaujsjsau/", admin.site.urls),
    ]
else:
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

    urlpatterns += [
        path("admin/", admin.site.urls),
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path("doc/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",),
    ]
