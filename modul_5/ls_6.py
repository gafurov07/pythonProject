import asyncio
import datetime

import sqlalchemy
import asyncpg
from sqlalchemy import Integer, Float, String, DateTime, Select, Insert
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Payment(Base):
    __tablename__ = "payments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    transaction_id: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(Integer)
    amount: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    def __str__(self):
        return f"{self.id} {self.transaction_id} {self.user_id} {self.amount} {self.status} {self.created_at} {self.updated_at}"


async def async_main():
    engine = create_async_engine("postgresql+asyncpg://postgres:1@localhost:5432/dvdrental")
    # async with engine.connect() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    #     await conn.commit()
    #     # await conn.run_sync(Base.metadata.drop_all)
    async with AsyncSession(engine) as session:

        payments = (await session.execute(Insert(Payment))).scalars()
        for payment in payments:
            print(payment)


asyncio.run(async_main())