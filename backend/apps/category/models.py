from django.db import models
from treebeard.mp_tree import MP_Node
from .managers import CategoryQuerySet


class Category(MP_Node):
    title = models.CharField(max_length=200, db_index=True)
    is_public = models.BooleanField(default=True)
    slug = models.SlugField()

    objects = CategoryQuerySet.as_manager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
