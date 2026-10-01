from sqlalchemy import Column, Integer, String, ForeignKey

from . import Base


class InspectionPhoto(Base):
    __tablename__ = "inspection_photos"

    id = Column(Integer, primary_key=True, index=True)
    inspection_id = Column(Integer, ForeignKey("inspections.id"), nullable=False)
    storage_path = Column(String(255), nullable=False)
    file_name = Column(String(255), nullable=False)