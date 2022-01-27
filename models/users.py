from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

    # selectin is used as it has no async query fetching problems with Pydantic nested models
    posts = relationship("Post", back_populates="user", lazy="selectin")
