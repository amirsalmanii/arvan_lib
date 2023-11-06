from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from drf_spectacular.utils import extend_schema
from apps.books.models import Book, BookGallery
from apps.books.serializers.admin import (
    BookListSerializer,
    BookCreateSerializer,
    BookGallerySerializer,
    BookRetrieveSerializer,
    BookModifySerializer,
)


class BookApiViewAdmin(APIView):
    @extend_schema(responses=BookListSerializer)
    def get(self, request):
        data = Book.objects.all()
        serializer = BookListSerializer(data, many=True, context={"request": request})
        return Response(serializer.data)

    @extend_schema(request=BookCreateSerializer, responses=BookListSerializer)
    def post(self, request):
        serializer = BookCreateSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class BookGallerySpiView(APIView):
    @extend_schema(request=BookGallerySerializer)
    def post(self, request):
        # TODO get book get 404 and good mode
        serializer = BookGallerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image = serializer.data.get("image")
        book_id = serializer.data.get("book")
        book = get_object_or_404(Book, pk=book_id)
        result = BookGallery.objects.create(book=book, image=image)
        return Response({})


class BookByIdApiViewAdmin(APIView):
    @extend_schema(responses=BookRetrieveSerializer)
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookRetrieveSerializer(book)
        return Response({"results": serializer.data})

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.status = "u"
        book.save()
        return Response()

    @extend_schema(request=BookModifySerializer, responses=BookModifySerializer)
    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookModifySerializer(instance=book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @extend_schema(request=BookModifySerializer, responses=BookModifySerializer)
    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookModifySerializer(instance=book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
