from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested

from .models import Author, Book


class AuthorSchema(SQLAlchemyAutoSchema):
    books = Nested(
        "BookSchema",
        many=True,
        only=("id", "title", "description", "created_by"),
        dump_only=True,
    )
    created_by = Nested("UserSchema", only=("id", "username"), dump_only=True)

    class Meta:
        model = Author
        include_relationships = True
        load_instance = True
        fields = ("id", "name", "description", "books", "created_by")


class BookSchema(SQLAlchemyAutoSchema):
    author = Nested(
        "AuthorSchema",
        only=("id", "name", "description", "created_by"),
        dump_only=True,
    )
    author_id = auto_field(load_only=True)
    created_by = Nested("UserSchema", only=("id", "username"), dump_only=True)

    class Meta:
        model = Book
        include_relationships = True
        load_instance = True
        fields = ("id", "title", "description", "author", "author_id", "created_by")
