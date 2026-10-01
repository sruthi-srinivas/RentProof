from sqlalchemy import Column, Integer, String, ForeignKey

from . import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    file_name = Column(String(255), nullable=False)
    storage_path = Column(String(255), nullable=False)
    document_type = Column(String(100), nullable=False)