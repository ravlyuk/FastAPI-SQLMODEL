from fastapi.openapi.models import Response
from starlette.requests import Request

from .services import set_last_activity, get_user_id


async def activity_monitor(request: Request, call_next) -> Response:
    response = await call_next(request)
    user_id = get_user_id(request)
    if user_id:
        await set_last_activity(user_id, 'last_activity')
    return response
