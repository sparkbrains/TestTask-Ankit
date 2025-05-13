from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List

from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.financial import FinancialRecordGroup
from app.views.financial import grouped_records_view

router = APIRouter(prefix="/api/financial-records", tags=["financial-records"])

@router.get("/", response_model=List[FinancialRecordGroup])
def financial_records(
    duration: str = Query(..., regex=r"^\d+\s*(day|days|week|weeks)$"),
    db: Session = Depends(get_db)
):
    try:
        return grouped_records_view(duration=duration, db=db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
