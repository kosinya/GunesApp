from datetime import datetime

from database import Base

from sqlalchemy import Column, String, Integer, Boolean, DateTime


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, index=True)
    name = Column(String(), nullable=False)
    date_of_birth = Column(String())
    phone_number = Column(String())
    email = Column(String(), unique=True, nullable=False, index=True)
    password = Column(String(), nullable=False)
    is_admin = Column(Boolean(), default=False, nullable=False)
    is_active = Column(Boolean(), default=False, nullable=False)


class Activation(Base):
    __tablename__ = 'activations'

    id = Column(Integer(), primary_key=True)
    user_email = Column(String(), unique=True, nullable=False, index=True)
    code = Column(String(), nullable=False)
    expiration_date = Column(String(), nullable=False)


class Reset(Base):
    __tablename__ = 'resets'

    id = Column(Integer(), primary_key=True)
    user_email = Column(String(), unique=True, nullable=False, index=True)
    code = Column(String(), nullable=False)
    date_of_creation = Column(String(), nullable=False)
    expiration_date = Column(String(), nullable=False)
