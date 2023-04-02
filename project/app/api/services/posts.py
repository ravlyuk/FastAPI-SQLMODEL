from datetime import datetime

from fastapi import HTTPException
from sqlalchemy import select

from app.models import Post


async def get_posts_service(session) -> [Post]:
    result = await session.execute(select(Post))
    posts = result.scalars().all()

    return posts


async def add_post_service(post, session, user) -> Post:
    post = Post(title=post.title, content=post.content, user=user)
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post


async def delete_post_service(post_id: int, session, user) -> dict:
    post = await get_post(session, post_id, user)
    await session.delete(post)
    await session.commit()
    return {"deleted": True}


async def update_post_service(post_id, post, session, user) -> Post:
    db_post = await get_post(session, post_id, user)

    post_data = post.dict(exclude_unset=True)
    for key, value in post_data.items():
        setattr(db_post, key, value)

    db_post.updated_at = datetime.utcnow()

    session.add(db_post)
    await session.commit()
    await session.refresh(db_post)
    return db_post


async def get_post(session, post_id: int, user) -> Post:
    post = await session.get(Post, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    elif post.user_id != user.id:
        raise HTTPException(status_code=401, detail="Forbidden. The post belongs to another user")

    return post
