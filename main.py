from fastapi import FastAPI
from router import sinhvien, account
from database import Base, engine
app=FastAPI()

Base.metadata.create_all(bind=engine)

for router in [
    sinhvien.router,
    account.router
]:
    app.include_router(router)
