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
