from sqlalchemy import Column, Integer, DateTime, ForeignKey, Date, DECIMAL, Computed

from app.db import Base


class Booking(Base):
    """
    Бронирование
    """

    __tablename__ = 'booking'
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(ForeignKey('room.id'))
    user_id = Column(ForeignKey('user.id'))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(DECIMAL, nullable=False)
    total_cost = Column(DECIMAL, Computed('(date_to - date_from) * price'))
    total_days = Column(Integer, Computed('date_to - date_from'))
