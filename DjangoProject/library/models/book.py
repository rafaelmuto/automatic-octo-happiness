from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    published_date = models.DateField(null=True)
    isbn = models.CharField(max_length=13, unique=True, null=True)

    def __str__(self):
        return f"Book({self.title}, {self.author}, {self.published_date} - ISBN: {self.isbn})"

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.published_date}, ISBN: {self.isbn})"

    def is_recently_published(self):
        from django.utils import timezone
        return self.published_date >= timezone.now().date() - timezone.timedelta(days=365)