from django.db import models


class BookQuerySet(models.QuerySet):
    def public(self):
        return self.exclude(status="u")
