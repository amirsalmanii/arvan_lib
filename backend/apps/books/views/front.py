from random import randint
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.books.models import Book
from drf_spectacular.utils import extend_schema
from apps.books.serializers.admin import (
    GalleryUploadSerializer,
)
from apps.books.serializers.front import (
    BookListSerializer,
    BookRetrieveSerializer,
)


def change_file_name(file_name):
    # TODO move good place
    new_file_name = randint(1111111111, 9999999999)
    file_names = file_name.split(".")
    ext = file_names[-1]
    finally_name = str(new_file_name) + "." + ext
    return finally_name


class FileUploadApiView(APIView):
    @extend_schema(request=GalleryUploadSerializer)
    def post(self, request):
        if file := request.FILES.get("file"):
            file_name = file.name
            new_file_name = change_file_name(file_name=file_name)
            path = default_storage.save(new_file_name, file)
            return Response({"results": path})
        return Response({"results": "err"})


class BookApiViewFront(APIView):
    @extend_schema(responses=BookListSerializer)
    def get(self, request):
        data = Book.objects.public()
        serializer = BookListSerializer(data, many=True, context={"request": request})
        return Response(serializer.data)


class BookByIdApiViewFront(APIView):
    @extend_schema(responses=BookListSerializer)
    def get(self, request, pk):
        data = Book.objects.public().filter(pk=pk)
        serializer = BookRetrieveSerializer(
            data, many=True, context={"request": request}
        )
        return Response(serializer.data)
