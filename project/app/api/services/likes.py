from fastapi import HTTPException

from app.models import Post


async def add_like_service(post_id, session):
    post = await session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    new_value = post.likes + 1
    setattr(post, 'likes', new_value)
    await session.commit()
    return post


async def add_dislike_service(post_id, session):
    post = await session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    new_value = post.dislikes + 1
    setattr(post, 'dislikes', new_value)
    await session.commit()
    return post
