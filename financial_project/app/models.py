from sqlalchemy import Column, String, Float, Date, Integer
from app.database import Base

class FinancialRecord(Base):
    __tablename__ = "financial_records"

    id = Column(Integer, primary_key=True, index=True)
    record_type = Column(String(3), nullable=False)
    name = Column(String(255), nullable=False)
    nav = Column(Float, nullable=True)
    created_at = Column(Date, nullable=False)
