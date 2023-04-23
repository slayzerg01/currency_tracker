from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from src.operations.router import get_specific_operations
from src.currency.router import get_tracked, get_exchange_rates
from src.database import get_async_session
from sqlalchemy import insert, select, desc
from src.currency.models import currency
import asyncio
import aiohttp

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
    difs = []

    for track in tracked:
        fc = str(track.first_currency)
        sc = str(track.second_currency)
        query = select(currency).where(currency.c.first_currency == fc, currency.c.second_currency == sc).order_by(
            desc(currency.c.date)).limit(2)
        res = await session.execute(query)
        tmp = res.all()
        if tmp:
            result.append(tmp[0])
            dif = None
            date = None
            if len(tmp) > 1:
                dif = tmp[1].value - tmp[0].value
                date = tmp[1].date
            difs.append([dif, date])
    combined_result = list(zip(result, difs))
    return templates.TemplateResponse("content.html", {"request": request, "results": combined_result})


# @router.get("/home/refresh/{currency1}-{currency2}")
# async def get_home_page(request: Request,
#                         tracked=Depends(get_tracked),
#                         session: AsyncSession = Depends(get_async_session)):
#     url = 'http://127.0.0.1:8000/currency/value'
#     for track in tracked:
#         fc = str(track.first_currency)
#         sc = str(track.second_currency)
#         params = {
#             'first_currency': fc,
#             'second_currency': sc,
#         }
#         async with aiohttp.ClientSession() as s:
#             async with s.get(url, params=params) as response:
#                 if response.status == 200:
#                     json_response = await response.json()
#                     value = json_response.get('value')
#                 else:
#                     print(f'Ошибка выполнения запроса. Код статуса: {response.status}')
#         query = select(currency).where(currency.c.first_currency == fc, currency.c.second_currency == sc).order_by(
#             desc(currency.c.date)).limit(2)
#         res = await session.execute(query)


@router.get("/home/refresh/{first_currency}-{second_currency}")
async def get_home_page(currency_value=Depends(get_exchange_rates)):
    try:
        return currency_value['value']
    except:
        return currency_value['error']
