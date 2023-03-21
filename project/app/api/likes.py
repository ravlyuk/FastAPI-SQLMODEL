from fastapi import APIRouter, HTTPException

from app.models import Post
from app.depends import CurrentUser, Session

like_router = APIRouter()


@like_router.post("/like/{post_id}", response_model=Post)
async def add_like(post_id: int, user: CurrentUser, session: Session):
    post = await session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    new_value = post.likes + 1
    setattr(post, 'likes', new_value)
    await session.commit()

    return post


@like_router.post("/dislike/{post_id}", response_model=Post)
async def add_dislike(post_id: int, user: CurrentUser, session: Session):
    post = await session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    new_value = post.dislikes + 1
    setattr(post, 'dislikes', new_value)
    await session.commit()
    return post
