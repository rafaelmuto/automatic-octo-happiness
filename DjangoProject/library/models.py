from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return f"Book({self.title}, {self.author}, {self.published_date} - ISBN: {self.isbn})"

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.published_date}, ISBN: {self.isbn})"

    def is_recently_published(self):
        from django.utils import timezone
        return self.published_date >= timezone.now().date() - timezone.timedelta(days=365)


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return f"Author({self.name}, {self.birth_date})"

    def __repr__(self):
        return f"Author({self.name}, {self.birth_date})"

class BookMark(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page_number = models.IntegerField()
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Bookmark for {self.book.title} at page {self.page_number}"

    def __repr__(self):
        return f"Bookmark({self.book.title}, Page: {self.page_number}, Note: {self.note})"