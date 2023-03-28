from fastapi import APIRouter

from app.api.services.likes import add_like_service, add_dislike_service
from app.models import Post
from app.depends import CurrentUser, Session

like_router = APIRouter(tags=['likes'])


@like_router.post("/like/{post_id}", response_model=Post)
async def add_like(post_id: int, user: CurrentUser, session: Session):
    return add_like_service(post_id, session)


@like_router.post("/dislike/{post_id}", response_model=Post)
async def add_dislike(post_id: int, user: CurrentUser, session: Session):
    return add_dislike_service(post_id, session)
