from sqlalchemy import Column, Integer, Date, ForeignKey, String

from . import Base


class Tenancy(Base):
    __tablename__ = "tenancies"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    status = Column(String(50), nullable=False)