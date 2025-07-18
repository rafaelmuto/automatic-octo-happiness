from rest_framework import serializers
from .models.author import Author
from .models.book import Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "birth_date", "death_date", "country"]

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ["id", "title", "author", "publish_date", "isbn"]

    def to_representation(self, instance):
        self.fields['author'] = AuthorSerializer(read_only=True)
        return super().to_representation(instance)

class AuthorDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "birth_date", "death_date", "country", "books"]
