from chalice_plus.permissions import IsAdmin, IsAuthenticated, IsOwnerOrAdmin
from chalice_plus.views import RetrieveUpdateDeleteView, CreateListView
from chalicelib.apps.users.authenticators import CustomCognitoAuthenticator
from sqlalchemy.orm import joinedload

from .models import Author, Book
from .schemas import AuthorSchema, BookSchema


class AuthorDetailView(RetrieveUpdateDeleteView):
    model = Author
    schema_class = AuthorSchema
    authenticator_class = CustomCognitoAuthenticator
    permission_classes = {
        "delete": [IsOwnerOrAdmin],
        "patch": [IsOwnerOrAdmin],
    }


class AuthorListView(CreateListView):
    model = Author
    schema_class = AuthorSchema
    authenticator_class = CustomCognitoAuthenticator
    permission_classes = {"post": [IsAuthenticated]}

    def load_object(self, *args, **kwargs):
        obj = super().load_object(*args, **kwargs)
        obj.created_by = self.authenticator.user
        return obj


class BookDetailView(RetrieveUpdateDeleteView):
    model = Book
    schema_class = BookSchema
    authenticator_class = CustomCognitoAuthenticator
    permission_classes = {
        "delete": [IsOwnerOrAdmin],
        "patch": [IsOwnerOrAdmin],
    }

    def get_object(self):
        if self.mask and "author" in self.mask:
            return self.session.query(self.model).filter_by(
                id=self.pk
            ).options(joinedload(Book.author)).first()
        return super().get_object()


class BookListView(CreateListView):
    model = Book
    schema_class = BookSchema
    authenticator_class = CustomCognitoAuthenticator
    permission_classes = {"post": [IsAuthenticated]}

    def load_object(self, *args, **kwargs):
        obj = super().load_object(*args, **kwargs)
        obj.created_by = self.authenticator.user
        return obj

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.mask and "author" in self.mask:
            return queryset.options(joinedload(Book.author))
        return queryset
