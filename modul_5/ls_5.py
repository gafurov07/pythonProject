# import requests
# from aiogram.utils.formatting import Email
# from sqlalchemy import create_engine, Integer, String, Float, JSON, Insert, Select, ForeignKey, asc, desc
# from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column, relationship, Session
#
# r = requests.get('https://dummyjson.com/users').json()
#
# engine = create_engine('postgresql://postgres:1@localhost:5432/dvdrental')
#
#
# class Base(DeclarativeBase):
#     @declared_attr
#     def __tablename__(self):
#         name = ''.join(map(lambda val: '_' * val.isupper() + val.lower(), self.__name__))
#         if name[-1] == 'y':
#             name = name[:-1] + 'ies'
#         else:
#             name += 's'
#         return name.lstrip('_')
#
#
# class Category2(Base):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String)
#     products: Mapped[list['Product']] = relationship('Product', back_populates='category')
#
#
# class Product(Base):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String)
#     category_id: Mapped[int] = mapped_column(Integer, ForeignKey('category2s.id', ondelete='CASCADE'))
#     category: Mapped['Category2'] = relationship('Category2', back_populates='products')
#     price: Mapped[float] = mapped_column(Float)
#
#
# def create_table():
#     Base.metadata.create_all(engine)
#
#
# def drop_table():
#     Base.metadata.drop_all(engine)
#
#
# def insert_data(_session: Session):
#     data = [{'name': 'oyn', 'category_id': 2, 'price': 1000}]
#     query = Insert(Product).values(data)
#     _session.execute(query)
#     _session.commit()
#
#
# if __name__ == '__main__':
#     # create_table()
#
#     with Session(engine) as session:
#
#         query2 = Select(Product).join(Category2, Category2.id == Product.category_id).order_by(desc(Product.price)).where(Product.price > 5000, Product.price < 10000)
#         for row in session.scalars(query2):
#             print(row.name, row.price, row.category.name)
#         # insert_data(session)
from datetime import datetime

import requests
from aiogram.utils.formatting import Email
from sqlalchemy import create_engine, Integer, String, Float, JSON, Insert, Select, ForeignKey, asc, desc, DateTime, \
    join
from sqlalchemy.dialects.postgresql import JSONB, array_agg
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column, relationship, Session, \
    declarative_base

r = requests.get('https://dummyjson.com/users').json()

engine = create_engine('postgresql://postgres:1@localhost:5432/dvdrental')

# class Base(DeclarativeBase):
#     @declared_attr
#     def __tablename__(self):
#         name = ''.join(map(lambda val: '_' * val.isupper() + val.lower(), self.__name__))
#         # if name[-1] == 'y':
#         #     name = name[:-1] + 'ies'
#         # else:
#         #     name += 's'
#         return name.lstrip('_')

Base = declarative_base()


class Actor(Base):
    __tablename__ = 'actor'
    actor_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    last_update: Mapped[datetime] = mapped_column(DateTime)


class Film(Base):
    __tablename__ = 'film'
    film_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    release_year: Mapped[int] = mapped_column(Integer)
    language_id: Mapped[int] = mapped_column(Integer)
    rental_duration: Mapped[int] = mapped_column(Integer)
    rental_rate: Mapped[float] = mapped_column(Float)
    length: Mapped[int] = mapped_column(Integer)
    replacement_cost: Mapped[float] = mapped_column(Float)
    rating: Mapped[str] = mapped_column(String)
    last_update: Mapped[datetime] = mapped_column(DateTime)
    special_features: Mapped[str] = mapped_column(String)
    fulltext: Mapped[dict] = mapped_column(JSONB)


class FilmActor(Base):
    __tablename__ = "film_actor"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    actor_id: Mapped[int] = mapped_column(Integer)
    film_id: Mapped[int] = mapped_column(Integer)
    last_updated: Mapped[datetime] = mapped_column(DateTime)


def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    # create_table()

    with Session(engine) as session:

        query2 = Select(Actor.actor_id, Actor.first_name, Actor.last_name, array_agg(Film.title)).select_from(join(FilmActor, Actor, Actor.actor_id == FilmActor.actor_id).join(Film, Film.film_id == FilmActor.film_id)).group_by(Actor.actor_id, Actor.last_name, Actor.first_name)
        res = session.execute(query2)
        for row in res:
            print(row)
        # insert_data(session)
