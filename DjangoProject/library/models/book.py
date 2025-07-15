from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    publish_date = models.DateField(null=True)
    publisher = models.CharField(max_length=100, null=True)
    number_of_pages = models.PositiveIntegerField(null=True, blank=True)

    isbn = models.CharField(max_length=13, unique=True, null=True)
    open_library_key = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self):
        return (
            f"Book({self.title}, {self.author}, {self.publish_date} - ISBN:{self.isbn})"
        )

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.publish_date}, {self.isbn})"

    def is_recently_published(self):
        from django.utils import timezone

        return self.publish_date >= timezone.now().date() - timezone.timedelta(days=365)
