from datetime import datetime
from typing import Optional

from fastapi_users_db_sqlmodel import SQLModelBaseUserDB
from pydantic import UUID4

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(SQLModelBaseUserDB, table=True):
    activity: Optional['Activity'] = Relationship(back_populates="user")
    posts: Optional['Post'] = Relationship(back_populates="user")


class Activity(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    last_login: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    last_activity: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    user_id: Optional[UUID4] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="activity")


class PostBase(SQLModel):
    title: str
    content: str


class Post(PostBase, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: Optional[UUID4] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="posts")

    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    likes: Optional['Like'] = Relationship(back_populates="posts")


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class LikeBase(SQLModel):
    post_id: int
    user_id: Optional[UUID4]


class LikeCreate(SQLModel):
    post_id: int


class Like(LikeBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    post_id: int = Field(default=None, foreign_key="post.id")
    user_id: UUID4 = Field(default=None, foreign_key="user.id")

    posts: Optional[Post] = Relationship(back_populates="likes")


class Dislike(LikeBase, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: Optional[UUID4] = Field(default=None, foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
