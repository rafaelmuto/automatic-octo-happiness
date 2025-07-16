from .author_views import AuthorDetail, AuthorCreate, AuthorUpdate, AuthorDelete, AuthorList
from .book_views import BookDetail, BookCreate, BookUpdate, BookDelete, BookListView, BookListByAuthorView

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
]