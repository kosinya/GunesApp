from sqlalchemy import Column, Integer, String

from database import Base


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(), unique=True, index=True)
    path = Column(String())
    url = Column(String())


class Audio(Base):
    __tablename__ = 'audios'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(), unique=True, index=True)
    path = Column(String())
    url = Column(String())


class Video(Base):
    __tablename__ = 'videos'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(), unique=True, index=True)
    path = Column(String())
    url = Column(String())
