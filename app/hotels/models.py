from sqlalchemy import Column, String, Integer, JSON, ForeignKey, DECIMAL

from app.db import Base


class Hotel(Base):
    """
    Отель
    """

    __tablename__ = 'hotel'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_qty = Column(Integer, nullable=False)
    image_id = Column(Integer)


class Room(Base):
    """
    Комната
    """

    __tablename__ = 'room'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(Integer, ForeignKey('hotel.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(DECIMAL, nullable=False)
    services = Column(JSON)
    quantity = Column(Integer, nullable=False)
    number = Column(Integer, nullable=False)
