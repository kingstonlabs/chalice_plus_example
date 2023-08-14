from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from .models import User


class UserSchema(SQLAlchemyAutoSchema):
    authors = Nested(
        "AuthorSchema",
        many=True,
        only=("id", "name", "books", "description"),
        dump_only=True,
    )
    books = Nested(
        "BookSchema",
        many=True,
        only=("id", "title", "author", "description"),
        dump_only=True,
    )

    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        fields = ("id", "username", "authors", "books")
