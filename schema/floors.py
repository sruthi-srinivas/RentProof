from sqlalchemy import Column, Integer, ForeignKey

from . import Base


class Floor(Base):
    __tablename__ = "floors"

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.id"), nullable=False)
    floor_number = Column(Integer, nullable=False)