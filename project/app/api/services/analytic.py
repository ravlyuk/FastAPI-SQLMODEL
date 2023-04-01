from typing import List, Dict

import sqlalchemy as sa

from app.models import PostLike, PostDislike


async def analytic_service(session, date_from, date_to) -> dict[str, List[Dict[str, int]]]:
    likes = (
        await session.execute(
            sa.select(
                [
                    sa.cast(PostLike.created_at, sa.Date).label('date'),
                    sa.func.count(PostLike.id),
                ]
            ).filter(PostLike.created_at >= date_from)
            .filter(PostLike.created_at <= date_to)
            .group_by(sa.cast(PostLike.created_at, sa.Date))
        )

    ).all()

    dislikes = (
        await session.execute(
            sa.select(
                [
                    sa.cast(PostDislike.created_at, sa.Date).label('date'),
                    sa.func.count(PostDislike.id),
                ]
            ).filter(PostDislike.created_at >= date_from)
            .filter(PostDislike.created_at <= date_to)
            .group_by(sa.cast(PostDislike.created_at, sa.Date))
        )

    ).all()

    return {
        'likes': likes,
        'dislikes': dislikes
    }
