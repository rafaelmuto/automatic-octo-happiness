from django.urls import path

from .views import book_views, author_views, data_management_views

app_name = "library"
urlpatterns = [
    path("", book_views.BookListView.as_view(), name="index"),
    path("books/<int:pk>/", book_views.BookDetail.as_view(), name="book_detail"),
    path("author/<int:author_id>/", book_views.BookListByAuthorView.as_view(), name="index_by_author"),
    path("authors/", author_views.AuthorList.as_view(), name="author_list"),
    path("authors/<int:pk>/", author_views.AuthorDetail.as_view(), name="author_detail"),
    path("authors/add/", author_views.AuthorCreate.as_view(), name="author_add"),
    path("authors/<int:pk>/edit/", author_views.AuthorUpdate.as_view(), name="author_edit"),
    path("books/add/", book_views.BookCreate.as_view(), name="book_add"),
    path("books/<int:pk>/edit/", book_views.BookUpdate.as_view(), name="book_edit"),
    path("authors/<int:pk>/delete/", author_views.AuthorDelete.as_view(), name="author_delete"),
    path("books/<int:pk>/delete/", book_views.BookDelete.as_view(), name="book_delete"),
    path("data/", data_management_views.data_management, name="data_management"),
]
