from datetime import datetime

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.models import Post, User, PostCreate, PostUpdate
from app.depends import CurrentUser, Session

post_router = APIRouter()


@post_router.get("/posts", response_model=list[Post])
async def get_posts(user: CurrentUser, session: Session):
    result = await session.execute(select(Post))
    posts = result.scalars().all()

    return [
        Post(
            title=post.title,
            content=post.content,
            likes=post.likes,
            id=post.id,
            author=post.author

        ) for post in posts
    ]


@post_router.post("/posts")
async def add_post(post: PostCreate, user: CurrentUser, session: Session):
    post = Post(title=post.title, content=post.content, author=user.id)
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post


@post_router.delete("/posts/{post_id}")
async def delete_post(post_id: int, user: CurrentUser, session: Session):
    post = await session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    elif post.author != user.id:
        raise HTTPException(status_code=401, detail="Forbidden. The post belongs to another user")

    await session.delete(post)
    await session.commit()
    return {"deleted": True}


@post_router.patch("/posts/{post_id}", response_model=Post)
async def update_post(post_id: int, post: PostUpdate, user: CurrentUser, session: Session):
    db_post = await session.get(Post, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    post_data = post.dict(exclude_unset=True)
    for key, value in post_data.items():
        setattr(db_post, key, value)

    db_post.updated_at = datetime.utcnow()

    session.add(db_post)
    await session.commit()
    await session.refresh(db_post)
    return db_post
