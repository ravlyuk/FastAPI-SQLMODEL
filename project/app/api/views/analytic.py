from datetime import date

from fastapi import APIRouter, Query

from app.api.services.analytic import analytic_service
from app.models import Post
from app.depends import CurrentUser, Session

analytic_router = APIRouter(tags=['statistic'])


@analytic_router.get("/analytic/", response_model=list[Post])
async def get_analytics(user: CurrentUser, session: Session, date_from: date = Query(...), date_to: date = Query(...)):
    return await analytic_service(session, date_from, date_to)
