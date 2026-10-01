from sqlalchemy import Column, Integer, Text, String, ForeignKey

from . import Base


class AIAnalysis(Base):
    __tablename__ = "ai_analysis"

    id = Column(Integer, primary_key=True, index=True)
    inspection_photo_id = Column(
        Integer,
        ForeignKey("inspection_photos.id"),
        nullable=False
    )
    result = Column(Text, nullable=False)
    status = Column(String(50), nullable=False)