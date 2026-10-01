from sqlalchemy import Column, Integer, String, ForeignKey

from . import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)
    room_name = Column(String(100), nullable=False)