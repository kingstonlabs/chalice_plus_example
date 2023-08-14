import uuid

from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from chalicelib.models import Base


class Author(Base):
    __tablename__ = "authors"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = Column(String, nullable=False)
    description = Column(Text(), nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    created_by = relationship("User", backref="authors")

    def __repr__(self):
        return f"<Author ({self.name})>"


class Book(Base):
    __tablename__ = "books"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    title = Column(String, nullable=False)
    description = Column(Text(), nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey('authors.id'), nullable=False)
    author = relationship("Author", backref="books")
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    created_by = relationship("User", backref="books")

    def __repr__(self):
        return f"<Book ({self.title})>"
