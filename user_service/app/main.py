from fastapi import FastAPI
from api.route_user import user

app = FastAPI()
app.include_router(user, prefix="/users", tags=["User Docs"])