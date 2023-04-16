from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.currency.models import currency, tracked
from sqlalchemy import insert, select
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from src.currency.schemas import Tracked

router = APIRouter(
    prefix="/currency",
    tags=["currency"]
)


@router.get("/value")
async def get_exchange_rates(
        first_currency: str,
        second_currency: str,
        session: AsyncSession = Depends(get_async_session)):
    try:
        response = requests.get(f"https://www.google.com/finance/quote/{first_currency}-{second_currency}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            div = soup.find("div", class_="YMlKec fxKbKc")
            if div:
                value = div.text
                stmt = insert(currency).values(
                    first_currency=first_currency,
                    second_currency=second_currency,
                    value=float(value),
                    date=datetime.utcnow())
                await session.execute(stmt)
                await session.commit()
                return {"value": value}
            else:
                return {"error": "Элемент не найден на странице"}
        else:
            return {"error": "Не удалось получить содержимое страницы"}
    except ConnectionError:
        return {"error": "Не удалось подключиться к сети"}


@router.post("/add_track/")
async def add_track(first_currency: str, second_currency: str, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(tracked).values(first_currency=first_currency.strip(),
                                      second_currency=second_currency.strip(),
                                      date_at=datetime.utcnow())
        await session.execute(stmt)
        await session.commit()
        print("added")
        return {"status": "success",
                "details": f"Added {first_currency}-{second_currency}"}
    except IntegrityError:
        print("not")
        await session.rollback()
        return {"error": "Данная запись уже существует в базе"}


@router.get("/get_tracked", response_model=List[Tracked])
async def get_tracked(session: AsyncSession = Depends(get_async_session)):
    query = select(tracked)
    result = await session.execute(query)
    return result.all()
