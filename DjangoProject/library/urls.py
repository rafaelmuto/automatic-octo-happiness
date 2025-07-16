from django.urls import path


import library.views


app_name = "library"
urlpatterns = [
    path("", library.views.BookListView.as_view(), name="index"),
    path("books/<int:pk>/", library.views.BookDetail.as_view(), name="book_detail"),
    path("author/<int:author_id>/", library.views.BookListByAuthorView.as_view(), name="index_by_author"),
    path("authors/", library.views.AuthorList.as_view(), name="author_list"),
    path("authors/<int:pk>/", library.views.AuthorDetail.as_view(), name="author_detail"),
    path("authors/add/", library.views.AuthorCreate.as_view(), name="author_add"),
    path("authors/<int:pk>/edit/", library.views.AuthorUpdate.as_view(), name="author_edit"),
    path("books/add/", library.views.BookCreate.as_view(), name="book_add"),
    path("books/<int:pk>/edit/", library.views.BookUpdate.as_view(), name="book_edit"),
    path("authors/<int:pk>/delete/", library.views.AuthorDelete.as_view(), name="author_delete"),
    path("books/<int:pk>/delete/", library.views.BookDelete.as_view(), name="book_delete"),
]
