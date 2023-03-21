from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .db import get_async_session
from .models import User
from .users import current_active_user

CurrentUser = Annotated[User, Depends(current_active_user)]
Session = Annotated[AsyncSession, Depends(get_async_session)]
