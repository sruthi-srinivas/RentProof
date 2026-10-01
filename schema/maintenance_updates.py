from sqlalchemy import Column, Integer, Text, String, DateTime, ForeignKey
from datetime import datetime

from . import Base


class MaintenanceUpdate(Base):
    __tablename__ = "maintenance_updates"

    id = Column(Integer, primary_key=True, index=True)
    maintenance_request_id = Column(
        Integer,
        ForeignKey("maintenance_requests.id"),
        nullable=False
    )
    update_text = Column(Text, nullable=False)
    status = Column(String(50), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow)