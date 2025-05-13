from sqlalchemy.orm import Session
from typing import List
from app.schemas.financial import FinancialRecordGroup, FinancialRecordOut
from app.models import FinancialRecord
from app.utils.financial_utils import get_grouped_financial_records

def grouped_records_view(duration: str, db: Session) -> List[FinancialRecordGroup]:
    return get_grouped_financial_records(duration, db)
