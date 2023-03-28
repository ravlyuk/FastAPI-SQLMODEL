from fastapi import APIRouter

from app.schemas import UserCreate, UserRead, UserUpdate
from app.users import auth_backend, fastapi_users

auth_router = APIRouter(tags=["auth"])

auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
)
auth_router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
)
auth_router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
)

user_router = APIRouter(tags=["user"])
user_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/user",
)
