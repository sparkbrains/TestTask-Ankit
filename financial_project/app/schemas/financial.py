from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import List, Optional

class FinancialRecordOut(BaseModel):
    record_type: str
    fund_name: str
    market_value: Optional[float]
    date: date

    model_config = ConfigDict(from_attributes=True)

class FinancialRecordGroup(BaseModel):
    range: str
    records: List[FinancialRecordOut]
