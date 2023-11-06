from django.urls import path
from apps.category.views.admin import CategoryApiViewAdmin, CategoryByIdApiViewAdmin
from apps.books.views.admin import (
    BookApiViewAdmin,
    BookGallerySpiView,
    BookByIdApiViewAdmin,
)

urlpatterns = [
    path("category/", CategoryApiViewAdmin.as_view(), name="category_admin_api_view"),
    path(
        "category/<int:pk>",
        CategoryByIdApiViewAdmin.as_view(),
        name="category_admin_by_id",
    ),
    path("book/", BookApiViewAdmin.as_view(), name="book_admin_api_view"),
    path("book/gallery/", BookGallerySpiView.as_view(), name="book_gallery_api_view"),
    path("book/<int:pk>/", BookByIdApiViewAdmin.as_view(), name="book_admin_api_view"),
]
