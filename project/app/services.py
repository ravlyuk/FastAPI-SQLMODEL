import os
from datetime import datetime

import jwt
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from .config import API_STR
from .db import engine
from .models import Activity, User


async def set_last_activity(user_id: str, action: str) -> None:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        result = await session.execute(select(Activity).where(Activity.user_id == user_id))
        activity = result.scalars().first()
        now = datetime.utcnow()

        if activity:
            setattr(activity, action, now)
            await session.commit()
        else:
            activity = Activity(last_login=now, last_activity=now, user_id=user_id)
            session.add(activity)
            await session.commit()
            await session.refresh(activity)


def get_user_id(request) -> str | None:
    endpoint = request.scope.get('path')
    authorization = request.headers.get('authorization')

    ignore_endpoints = (
        API_STR + '/auth/jwt/login',
        API_STR + '/auth/register'
    )

    if not authorization or endpoint in ignore_endpoints:
        return None

    token = authorization.split(' ')[-1]
    try:
        decoded_token = jwt.decode(jwt=token, key=os.environ.get("SECRET"), options={"verify_signature": False})
    except jwt.exceptions.DecodeError:
        print("Invalid Token")
        return None
    user_id = decoded_token.get('sub')

    return user_id
