from django.urls import path
from apps.category.views.admin import CategoryApiViewAdmin, CategoryByIdApiViewAdmin

urlpatterns = [
    path("category/", CategoryApiViewAdmin.as_view(), name="category_admin_api_view"),
    path(
        "category/<int:pk>",
        CategoryByIdApiViewAdmin.as_view(),
        name="category_admin_by_id",
    ),
]
