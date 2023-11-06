from collections.abc import Iterable
from django.db import models
from apps.base.models import BaseModel
from apps.category.models import Category
from apps.books.managers import BookQuerySet


class STATUS(models.TextChoices):
    deleted = "d", "Deleted"
    borrowed = "b", "Borrowed"
    available = "a", "Available"
    unavailable = "u", "UnAvailable"


class Book(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=20)
    status = models.CharField(
        max_length=1, choices=STATUS.choices, default=STATUS.available
    )
    categories = models.ManyToManyField(Category, related_name="books")
    objects = BookQuerySet.as_manager()

    def __str__(self) -> str:
        return self.title[:20]


class BookGallery(BaseModel):
    book = models.ForeignKey(Book, related_name="gallery", on_delete=models.CASCADE)
    image = models.ImageField()
    image_url = models.CharField(max_length=250, null=True, blank=True)

    def save(self, *args, **kwargs):
        from apps.books.views.front import change_file_name

        object_storage_path = "https://storage.iran.liara.space/arvan-lib/"
        if self.image:
            # new_name = change_file_name(str(self.image))
            # self.image = new_name
            self.image_url = object_storage_path + str(self.image).replace(" ", "_")
        super(BookGallery, self).save(*args, **kwargs)
