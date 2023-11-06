from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from apps.category.models import Category
from apps.books.models import Book


class BookGalleryNestedInBooks(serializers.Serializer):
    image_url = serializers.CharField()


class NestedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "slug")


class BookListSerializer(serializers.ModelSerializer):
    categories = NestedCategorySerializer(many=True)
    gallery = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "description",
            "isbn",
            "status",
            "categories",
            "gallery",
        )

    @extend_schema_field({"example": [{"image_url": "string"}]})
    def get_gallery(self, book):
        galleries = book.gallery.all()
        gallery_data = BookGalleryNestedInBooks(galleries, many=True).data
        return gallery_data


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "description", "isbn", "status", "categories")
        read_only_fields = ("id",)


class GalleryUploadSerializer(serializers.Serializer):
    file = serializers.ImageField()


class BookGallerySerializer(serializers.Serializer):
    image = serializers.CharField()
    book = serializers.CharField()


class BookRetrieveSerializer(serializers.ModelSerializer):
    categories = NestedCategorySerializer(many=True)
    gallery = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "description",
            "isbn",
            "status",
            "categories",
            "gallery",
        )

    @extend_schema_field({"example": [{"image_url": "string"}]})
    def get_gallery(self, book):
        galleries = book.gallery.all()
        gallery_data = BookGalleryNestedInBooks(galleries, many=True).data
        return gallery_data


class BookModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "description", "isbn", "status", "categories")


# TODO update books gallery
