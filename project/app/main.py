from fastapi import FastAPI

from .api.views import (activity_router, analytic_router, like_router, post_router, user_router, auth_router)
from .middlewares import activity_monitor
from .config import API_STR

app = FastAPI(title="FastAPI Simple Blog", description="Test task.", version="0.1.0")
app.middleware("http")(activity_monitor)

for api_router in auth_router, user_router, post_router, like_router, activity_router, analytic_router:
    app.include_router(api_router, prefix=API_STR)
