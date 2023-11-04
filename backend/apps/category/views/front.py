from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from .admin import CategoryApiViewAdmin, CategoryByIdApiViewAdmin


class CategoryApiViewFront(APIView):
    @extend_schema(responses=CategoryApiViewAdmin.CategoryTreeSerializer)
    def get(self, request):
        return CategoryApiViewAdmin.get(self, request, public=True)


class CategoryByIdApiViewFront(APIView):
    @extend_schema(
        responses=CategoryByIdApiViewAdmin.CategoryNodeSerializer,
    )
    def get(self, request, pk):
        return CategoryByIdApiViewAdmin.get(self, request, pk)
