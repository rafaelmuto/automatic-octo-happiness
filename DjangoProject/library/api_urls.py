from django.urls import path

from .api import author_api, book_api, openlibrary_api

urlpatterns = [
    path("books/", book_api.BookListAPIView.as_view(), name="book-list"),
    path("books/<str:isbn>/", book_api.BookDetailAPIView.as_view(), name="book-detail"),
    path("authors/", author_api.AuthorListAPIView.as_view(), name="author-list"),
    path("authors/<int:pk>/", author_api.AuthorDetailAPIView.as_view(), name="author-detail"),
    path("authors/name/<str:name>/", author_api.AuthorSearchAPIView.as_view(), name="author-search"),
    path("openlibrary/isbn/<str:isbn>/", openlibrary_api.search_by_isbn_view, name="openlibrary-isbn"),
    path("openlibrary/key/<str:key>/", openlibrary_api.get_data_by_key_view, name="openlibrary-key"),
]
