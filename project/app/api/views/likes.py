from fastapi import APIRouter

from app.api.services.likes import add_like_or_dislike_service
from app.models import PostLikeBase, PostLike, PostDislike
from app.depends import CurrentUser, Session

like_router = APIRouter(tags=['likes'])


@like_router.post("/like/", response_model=PostLikeBase)
async def add_like(post_like_create: PostLikeBase, user: CurrentUser, session: Session):
    return await add_like_or_dislike_service(post_like_create, PostLike, session)


@like_router.post("/dislike/", response_model=PostLikeBase)
async def add_dislike(post_dislike_create: PostLikeBase, user: CurrentUser, session: Session):
    return await add_like_or_dislike_service(post_dislike_create, PostDislike, session)
