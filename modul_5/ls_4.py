import requests
from aiogram.utils.formatting import Email
from sqlalchemy import create_engine, Integer, String, Float, JSON
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

r = requests.get('https://dummyjson.com/users').json()

engine = create_engine('postgresql://postgres:1@localhost:5432/dvdrental')


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(self):
        name = ''.join(map(lambda val: '_' * val.isupper() + val.lower(), self.__name__))
        if name[-1] == 'y':
            name = name[:-1] + 'ies'
        else:
            name += 's'
        return name.lstrip('_')

class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    maiden_name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    phone: Mapped[int] = mapped_column(Integer)
    username: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    birthdate: Mapped[str] = mapped_column(String)
    image: Mapped[str] = mapped_column(String)
    blood_group: Mapped[str] = mapped_column(String)
    height: Mapped[int] = mapped_column(Integer)
    weight: Mapped[float] = mapped_column(Float)
    eye_color: Mapped[str] = mapped_column(String)
    hair: Mapped[dict] = mapped_column(JSON)
    domain: Mapped[str] = mapped_column(String)
    ip: Mapped[str] = mapped_column(String)
    address: Mapped[dict] = mapped_column(JSON)
    mac_address: Mapped[str] = mapped_column(String)
    university: Mapped[str] = mapped_column(String)
    bank: Mapped[dict] = mapped_column(JSON)
    card_number: Mapped[str] = mapped_column(String)
    card_type: Mapped[str] = mapped_column(String)
    currency: Mapped[str] = mapped_column(String)
    





print(r['users'][0])
