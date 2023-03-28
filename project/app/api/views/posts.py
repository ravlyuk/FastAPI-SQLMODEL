from fastapi import APIRouter

from app.api.services.posts import get_posts_service, add_post_service, delete_post_service, update_post_service
from app.models import Post, User, PostCreate, PostUpdate
from app.depends import CurrentUser, Session

post_router = APIRouter(tags=['posts'])


@post_router.get("/posts", response_model=list[Post])
async def get_posts(user: CurrentUser, session: Session):
    return get_posts_service(session)


@post_router.post("/posts")
async def add_post(post: PostCreate, user: CurrentUser, session: Session):
    return add_post_service(session, user, post)


@post_router.delete("/posts/{post_id}")
async def delete_post(post_id: int, user: CurrentUser, session: Session):
    return delete_post_service(post_id, user, session)


@post_router.patch("/posts/{post_id}", response_model=Post)
async def update_post(post_id: int, post: PostUpdate, user: CurrentUser, session: Session):
    return update_post_service(post_id, post, session)
