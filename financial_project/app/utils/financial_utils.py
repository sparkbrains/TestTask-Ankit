import re
from datetime import timedelta
from sqlalchemy.orm import Session
from typing import List
from app.models import FinancialRecord
from app.schemas.financial import FinancialRecordOut, FinancialRecordGroup

def get_grouped_financial_records(duration: str, db: Session) -> List[FinancialRecordGroup]:
    pattern = re.fullmatch(r"(\d+)\s*(day|days|week|weeks)", duration.strip().lower())
    if not pattern:
        raise ValueError("Invalid duration format. Use ?duration=2days, 1week, etc.")

    value, unit = int(pattern.group(1)), pattern.group(2)
    day_chunk = value * 7 if unit.startswith("week") else value

    all_records = db.query(FinancialRecord).order_by(FinancialRecord.created_at).all()
    if not all_records:
        return []

    start_date = all_records[0].created_at
    end_date = all_records[-1].created_at

    result = []
    current_start = start_date

    while current_start <= end_date:
        current_end = current_start + timedelta(days=day_chunk - 1)
        chunk = db.query(FinancialRecord).filter(
            FinancialRecord.created_at.between(current_start, current_end)
        ).all()

        result.append(FinancialRecordGroup(
            range=f"{current_start} to {current_end}",
            records=[
                FinancialRecordOut(
                    record_type=r.record_type,
                    fund_name=r.name,
                    market_value=r.nav,
                    date=r.created_at
                )
                for r in chunk
            ]
        ))

        current_start = current_end + timedelta(days=1)

    return result
