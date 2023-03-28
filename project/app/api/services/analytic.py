from sqlalchemy import select, and_, func

from app.models import Post


async def analytic_service(session, date_from, date_to):
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
