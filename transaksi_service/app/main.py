from fastapi import FastAPI
from api.route_transaksi import transaksi

app = FastAPI()
app.include_router(transaksi, prefix="/transactions", tags=["transaksi Docs"])