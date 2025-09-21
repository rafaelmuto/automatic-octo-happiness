from django.db import models


class BookMark(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    page_number = models.IntegerField()
    note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Bookmark for {self.book.title} at page {self.page_number}"

    def __repr__(self):
        return (
            f"Bookmark({self.book.title}, Page: {self.page_number}, Note: {self.note})"
        )
