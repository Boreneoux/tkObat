from fastapi import FastAPI
from api.route_obat import obat

app = FastAPI()
app.include_router(obat, prefix="/obats", tags=["obat Docs"])