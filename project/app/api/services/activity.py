from sqlalchemy import select

from app.models import Activity


async def activity_service(user, session):
    result = await session.execute(select(Activity).where(Activity.user == user))

    return result.scalars().all()
