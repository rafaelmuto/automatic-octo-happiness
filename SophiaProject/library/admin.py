from django.contrib import admin
from .models import Book, Author, BookMark

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookMark)
