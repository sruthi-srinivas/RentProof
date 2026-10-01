from sqlalchemy import Column, Integer, Text, String, ForeignKey

from . import Base


class MaintenanceRequest(Base):
    __tablename__ = "maintenance_requests"

    id = Column(Integer, primary_key=True, index=True)
    issue_id = Column(Integer, ForeignKey("issues.id"), nullable=False)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), nullable=False)
    priority = Column(String(50), nullable=False)