from fastapi import FastAPI
from fastapi.openapi.models import Response

from starlette.requests import Request

from .api import (activity_router, analytic_router, like_router, post_router, user_router)
from .services import set_last_activity, get_user_id

app = FastAPI(title="FastAPI Simple Blog", description="Test task for Mint company.", version="0.1.0")
API_V1_STR = '/api/v1'


@app.middleware("http")
async def activity_monitor(request: Request, call_next) -> Response:
    response = await call_next(request)
    user_id = get_user_id(request)
    if user_id:
        await set_last_activity(user_id, 'last_activity')
    return response


for api_router in activity_router, analytic_router, like_router, post_router, user_router:
    app.include_router(api_router, prefix=API_V1_STR)
