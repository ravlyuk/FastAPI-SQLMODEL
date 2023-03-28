from fastapi import APIRouter

from app.depends import CurrentUser, Session

from app.api.services.activity import activity_service

activity_router = APIRouter(tags=['statistic'])


@activity_router.get("/activity/")
async def get_activity(user: CurrentUser, session: Session):
    return await activity_service(user, session)
