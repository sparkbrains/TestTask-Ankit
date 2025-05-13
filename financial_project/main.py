from fastapi import FastAPI
from app.database import Base, engine
from app.routers import financial

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(financial.router)
