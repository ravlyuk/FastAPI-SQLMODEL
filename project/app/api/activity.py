from fastapi import APIRouter
from sqlalchemy import select

from app.depends import CurrentUser, Session
from app.models import Activity

activity_router = APIRouter()


@activity_router.get("/activity/")
async def get_activity(user: CurrentUser, session: Session):
    result = await session.execute(select(Activity).where(Activity.user == user))

    return result.scalars().all()
