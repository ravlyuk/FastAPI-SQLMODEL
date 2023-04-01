from datetime import datetime
from typing import Optional

from fastapi_users_db_sqlmodel import SQLModelBaseUserDB
from pydantic import UUID4

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(SQLModelBaseUserDB, table=True):
    activity: Optional["Activity"] = Relationship(back_populates="user")


class Activity(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    last_login: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    last_activity: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    user_id: Optional[UUID4] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="activity")


class PostBase(SQLModel):
    title: str
    content: str
    author: Optional[UUID4]


class Post(PostBase, table=True):
    id: int = Field(default=None, primary_key=True)
    likes: Optional[int] = Field(default=0)
    dislikes: Optional[int] = Field(default=0)

    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class PostLikeBase(SQLModel):
    post_id: int
    user_id: int


class PostLike(PostLikeBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class PostDislike(PostLikeBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
