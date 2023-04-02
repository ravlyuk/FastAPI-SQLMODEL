from typing import List, Dict

import sqlalchemy as sa

from app.models import Like, Dislike


async def analytic_service(session, date_from, date_to) -> dict[str, List[Dict[str, int]]]:
    likes = (
        await session.execute(
            sa.select(
                [
                    sa.cast(Like.created_at, sa.Date).label('date'),
                    sa.func.count(Like.id),
                ]
            ).filter(Like.created_at >= date_from)
            .filter(Like.created_at <= date_to)
            .group_by(sa.cast(Like.created_at, sa.Date))
        )

    ).all()

    dislikes = (
        await session.execute(
            sa.select(
                [
                    sa.cast(Dislike.created_at, sa.Date).label('date'),
                    sa.func.count(Dislike.id),
                ]
            ).filter(Dislike.created_at >= date_from)
            .filter(Dislike.created_at <= date_to)
            .group_by(sa.cast(Dislike.created_at, sa.Date))
        )

    ).all()

    return {
        'likes': likes,
        'dislikes': dislikes
    }
