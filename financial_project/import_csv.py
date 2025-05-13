import pandas as pd
from app.database import SessionLocal, engine, Base
from app.models import FinancialRecord

Base.metadata.create_all(bind=engine)

def import_csv(path):
    print("Starting CSV import...")
    df = pd.read_csv(path, parse_dates=["created_at"])
    db = SessionLocal()
    records = [
        FinancialRecord(
            record_type="mf",
            name=row.fund_name,
            nav=row.nav,
            created_at=row.created_at.date()
        ) for row in df.itertuples(index=False)
    ]
    db.bulk_save_objects(records)
    db.commit()
    print(f"Imported {len(records)} records.")

if __name__ == "__main__":
    import_csv("realistic_mutual_fund_data_365days.csv")

