import uuid

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from chalicelib.models import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    username = Column(String(64), unique=True)
    email = Column(String(256), unique=True)
    is_superuser = Column(Boolean, default=False)
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<User (name='{self.username}', email='{self.email}')>"
