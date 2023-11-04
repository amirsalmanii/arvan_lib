from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from apps.category.views.front import CategoryApiViewFront, CategoryByIdApiViewFront


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("valid/token/", TokenVerifyView.as_view(), name="token_verify"),
    path("category/", CategoryApiViewFront.as_view(), name="category_front_api_view"),
    path(
        "category/<int:pk>",
        CategoryByIdApiViewFront.as_view(),
        name="category_front_by_id",
    ),
]
