from sqlalchemy import Column, Integer, String, ForeignKey

from . import Base


class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, index=True)
    floor_id = Column(Integer, ForeignKey("floors.id"), nullable=False)
    unit_number = Column(String(50), nullable=False)