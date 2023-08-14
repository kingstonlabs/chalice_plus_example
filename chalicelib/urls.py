from chalicelib.apps.books.views import (
    AuthorDetailView, AuthorListView, BookDetailView, BookListView,
)
from chalicelib.apps.users.views import UserDetailView, UserListView


urlpatterns = [
    ("/authors", AuthorListView.as_view()),
    ("/authors/{uuid:id}", AuthorDetailView.as_view()),
    ("/books", BookListView.as_view()),
    ("/books/{uuid:id}", BookDetailView.as_view()),
    ("/users", UserListView.as_view()),
    ("/users/{uuid:id}", UserDetailView.as_view()),
]
