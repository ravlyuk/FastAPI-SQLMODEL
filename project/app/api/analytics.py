from datetime import date

from fastapi import APIRouter, Query
from sqlalchemy import select, and_, func

from app.models import Post
from app.depends import CurrentUser, Session

analytics_router = APIRouter(tags=['statistic'])


@analytics_router.get("/analytics/", response_model=list[Post])
async def get_analytics(user: CurrentUser, session: Session,  date_from: date = Query(...), date_to: date = Query(...)):
    result = await session.execute(select(Post).where(
        and_(Post.created_at >= date_from, Post.created_at <= date_to)
    ).order_by(
        func.date(Post.created_at)
    ))

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
