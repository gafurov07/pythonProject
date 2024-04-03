from sqlalchemy import create_engine, Integer, String, ForeignKey, Insert, Select
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr, Session, relationship

url = 'https://dummyjson.com/products'


# Base = declarative_base()

class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(self):
        name = ''.join(map(lambda val: '_' * val.isupper() + val.lower(), self.__name__))
        if name[-1] == 'y':
            name = name[:-1] + 'ies'
        else:
            name += 's'
        return name.lstrip('_')


engine = create_engine('postgresql://postgres:1@localhost:5432/dvdrental')


class EduCenter(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    course: Mapped[str] = mapped_column(String)
    student: Mapped['Student'] = relationship('Student', back_populates='edu')


class Student(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    edu_id: Mapped[int] = mapped_column(Integer, ForeignKey('edu_centers.id', ondelete='CASCADE'))
    edu: Mapped['EduCenter'] = relationship('EduCenter', back_populates='student')


def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


def insert_data(_session: Session):
    data = [{'name': 'Nurik', 'edu_id': 1}]
    query = Insert(Student).values(data)
    _session.execute(query)
    _session.commit()


if __name__ == '__main__':
    # drop_table()
    # create_table()

    with Session(engine) as session:
        query2 = Select(Student)
        for student in session.scalars(query2):
            print(student.edu.name)

        # insert_data(session)
