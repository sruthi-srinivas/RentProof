from sqlalchemy import Column, Integer, Text, String, ForeignKey

from . import Base


class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    inspection_id = Column(Integer, ForeignKey("inspections.id"), nullable=False)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    severity = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)