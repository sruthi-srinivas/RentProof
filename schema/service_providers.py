from sqlalchemy import Column, Integer, String, Text

from . import Base


class ServiceProvider(Base):
    __tablename__ = "service_providers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    service_type = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(150), nullable=True)
    description = Column(Text, nullable=True)