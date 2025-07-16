from .author_views import AuthorDetail, AuthorCreate, AuthorUpdate, AuthorDelete, AuthorList
from .book_views import BookDetail, BookCreate, BookUpdate, BookDelete, BookListView, BookListByAuthorView
from .data_management_views import data_management

__all__ = [
    "AuthorDetail",
    "AuthorCreate",
    "AuthorUpdate",
    "AuthorDelete",
    "AuthorList",
    "BookDetail",
    "BookCreate",
    "BookUpdate",
    "BookDelete",
    "BookListView",
    "BookListByAuthorView",
    "data_management",
]