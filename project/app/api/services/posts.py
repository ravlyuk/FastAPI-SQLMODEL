from datetime import datetime

from fastapi import HTTPException
from sqlalchemy import select

from app.models import Post


async def get_posts_service(session) -> [Post]:
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


async def add_post_service(post, session, user) -> Post:
    post = Post(title=post.title, content=post.content, author=user.id)
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post


async def delete_post_service(post_id, session, user) -> dict:
    post = await session.get(Post, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    elif post.author != user.id:
        raise HTTPException(status_code=401, detail="Forbidden. The post belongs to another user")

    await session.delete(post)
    await session.commit()
    return {"deleted": True}


async def update_post_service(post_id, post, session, user) -> Post:
    db_post = await session.get(Post, post_id)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    elif db_post.author != user.id:
        raise HTTPException(status_code=401, detail="Forbidden. The post belongs to another user")

    post_data = post.dict(exclude_unset=True)
    for key, value in post_data.items():
        setattr(db_post, key, value)

    db_post.updated_at = datetime.utcnow()

    session.add(db_post)
    await session.commit()
    await session.refresh(db_post)
    return db_post
