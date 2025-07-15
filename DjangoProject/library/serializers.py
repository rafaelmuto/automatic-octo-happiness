from rest_framework import serializers
from .models.author import Author
from .models.book import Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publish_date', 'isbn']
