from sqlalchemy import Column, String, create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    # table name
    __tablename__ = 'user'

    # table structure
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # 1-multiply
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    user_id = Column(String(20), ForeignKey('user.id'))


engine = create_engine('mysql+mysqlconnector://root:zh123ling@localhost:3306/test')

DBSession = sessionmaker(bind=engine)


# class School(Base):
#     __tablename__ = 'school'
#     id = ...
#     name = ...


# insert
def insert():
    session = DBSession()

    new_user = User(id='77', name='ZLY')

    session.add(new_user)

    session.commit()

    session.close()


# query
def query():
    session = DBSession()
    user = session.query(User).filter(User.id == '77').one()

    print('type:', type(user))
    print('name:', user.name)
    session.close()


# insert()
query()
