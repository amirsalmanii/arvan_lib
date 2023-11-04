from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from apps.category.permissions import IsAdmin
from drf_spectacular.utils import extend_schema, extend_schema_field
from drf_spectacular.types import OpenApiTypes
from ..models import Category


class CategoryApiViewAdmin(APIView):
    class CategoryCreateSerializer(serializers.ModelSerializer):
        parent = serializers.IntegerField(required=False)

        def create(self, validated_data):
            slug = validated_data.get("title").replace(" ", "-")
            parent = validated_data.pop("parent", None)
            validated_data.update({"slug": slug})
            if parent is None:
                instance = Category.add_root(**validated_data)
            else:
                parent_node = get_object_or_404(Category, pk=parent)
                instance = parent_node.add_child(**validated_data)
            return instance

        class Meta:
            model = Category
            fields = ("title", "is_public", "slug", "parent")
            extra_kwargs = {"slug": {"required": False}}

    class CategoryTreeSerializer(serializers.ModelSerializer):
        children = serializers.SerializerMethodField()

        @extend_schema_field(serializers.ListField())
        def get_children(self, obj):
            return CategoryApiViewAdmin.CategoryTreeSerializer(
                obj.get_children(), many=True
            ).data

        class Meta:
            model = Category
            fields = ("id", "title", "is_public", "slug", "children")

    def get_permissions(self):
        return [IsAdmin()]

    @extend_schema(request=CategoryCreateSerializer, responses=CategoryCreateSerializer)
    def post(self, request):
        serializer = CategoryApiViewAdmin.CategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(CategoryApiViewAdmin.CategoryCreateSerializer(instance).data)

    @extend_schema(responses=CategoryTreeSerializer)
    def get(self, request, public=None):
        if public is None:
            data = Category.objects.filter(depth=1)
        else:
            data = Category.objects.public().filter(depth=1)
        serializer = CategoryApiViewAdmin.CategoryTreeSerializer(data, many=True)
        return Response(serializer.data)


class CategoryByIdApiViewAdmin(APIView):
    class CategoryNodeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ("id", "title", "is_public", "slug")

    class CategoryModifySerializer(serializers.ModelSerializer):
        def update(self, instance, validated_data):
            if title := validated_data.get("title"):
                slug = title.replace(" ", "-")
                validated_data.update({"slug": slug})
            return super().update(instance=instance, validated_data=validated_data)

        class Meta:
            model = Category
            fields = ("title", "is_public")

    def get_permissions(self):
        return [IsAdmin()]

    @extend_schema(
        responses=CategoryNodeSerializer,
    )
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategoryByIdApiViewAdmin.CategoryNodeSerializer(category)
        print(category)
        return Response(serializer.data)

    @extend_schema(responses=CategoryModifySerializer, request=CategoryModifySerializer)
    def patch(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategoryByIdApiViewAdmin.CategoryModifySerializer(
            instance=category, data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @extend_schema(responses=CategoryModifySerializer, request=CategoryModifySerializer)
    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategoryByIdApiViewAdmin.CategoryModifySerializer(
            instance=category, data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=204)
