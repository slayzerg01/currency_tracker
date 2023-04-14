from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, Float, UniqueConstraint
from sqlalchemy import MetaData

metadata = MetaData()

currency = Table(
    "currency",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_currency", String, nullable=False),
    Column("second_currency", String, nullable=False),
    Column("value", Float, nullable=False),
    Column("date", TIMESTAMP, nullable=False),
)

tracked = Table(
    "tracked",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_currency", String, nullable=False),
    Column("second_currency", String, nullable=False),
    Column("date_at", TIMESTAMP, nullable=False),
    UniqueConstraint("first_currency", "second_currency", name="_first_currency_second_currency_uc"),
)
