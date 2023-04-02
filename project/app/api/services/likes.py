import sqlalchemy as sa
from fastapi import HTTPException

from app.models import Like, Dislike, Post


async def add_like_service(post_like, user, session) -> Like:
    await check_post(session, post_like)
    post_like_db = await session.execute(
        sa.select(Like).filter(Like.post_id == post_like.post_id and Like.user_id == user.id)
    )
    is_exist = post_like_db.scalar()

    if is_exist:
        raise HTTPException(status_code=400,
                            detail=f'User {user.id} already added like for post ID: {post_like.post_id}')
    post_like_create = Like(post_id=post_like.post_id, user_id=user.id)
    session.add(post_like_create)
    await session.commit()
    await session.refresh(post_like_create)
    return post_like_create


async def add_dislike_service(post_dislike, user, session) -> Dislike:
    await check_post(session, post_dislike)
    post_dislike_db = await session.execute(
        sa.select(Dislike).where(Dislike.post_id == post_dislike.post_id and Dislike.user_id == user.id)
    )
    is_exist = post_dislike_db.scalar()
    if is_exist:
        raise HTTPException(status_code=400,
                            detail=f'User {user.id} already added dislike for post ID: {post_dislike.post_id}')

    post_like_create = Dislike(post_id=post_dislike.post_id, user_id=user.id)
    session.add(post_like_create)
    await session.commit()
    await session.refresh(post_like_create)
    return post_like_create


async def check_post(session, post_like) -> None:
    post = await session.get(Post, post_like.post_id)
    if post is None:
        raise HTTPException(status_code=400, detail=f"Post {post_like.post_id} not found")
