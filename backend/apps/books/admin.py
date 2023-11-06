from django.contrib import admin
from apps.books.models import Book, BookGallery


class BookGalleryAdmin(admin.StackedInline):
    model = BookGallery


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = (BookGalleryAdmin,)
    list_display = ("id", "title", "status")
