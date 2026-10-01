from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from datetime import datetime

from . import Base


class Inspection(Base):
    __tablename__ = "inspections"

    id = Column(Integer, primary_key=True, index=True)
    tenancy_id = Column(Integer, ForeignKey("tenancies.id"), nullable=False)
    inspection_type = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    inspected_at = Column(DateTime, default=datetime.utcnow)