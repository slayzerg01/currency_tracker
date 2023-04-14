from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from src.operations.router import get_specific_operations
from src.currency.router import get_tracked, get_exchange_rates
from src.database import get_async_session
from sqlalchemy import insert, select, desc
from src.currency.models import currency

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/search/{operation_type}")
def get_search_page(request: Request, operations=Depends(get_specific_operations)):
    return templates.TemplateResponse("search.html", {"request": request, "operations": operations})


@router.get("/home")
async def get_home_page(request: Request,
                        tracked=Depends(get_tracked),
                        session: AsyncSession = Depends(get_async_session)):
    result = []
    for track in tracked:
        fc = str(track.first_currency)
        sc = str(track.second_currency)
        query = select(currency).where(currency.c.first_currency == fc, currency.c.second_currency == sc).order_by(desc(currency.c.date)).limit(1)
        res = await session.execute(query)
        tmp = res.all()
        if tmp:
            for t in tmp:
                result.append(t)
    print(result)
    return templates.TemplateResponse("content.html", {"request": request, "results": result})
