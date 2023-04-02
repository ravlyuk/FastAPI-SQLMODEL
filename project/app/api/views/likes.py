from fastapi import APIRouter

from app.api.services.likes import add_like_service, add_dislike_service
from app.models import LikeCreate
from app.depends import CurrentUser, Session

like_router = APIRouter(tags=['likes'])


@like_router.post("/like/")
async def add_like(like: LikeCreate, user: CurrentUser, session: Session):
    return await add_like_service(like, user, session)


@like_router.post("/dislike/")
async def add_dislike(dislike: LikeCreate, user: CurrentUser, session: Session):
    return await add_dislike_service(dislike, user, session)
