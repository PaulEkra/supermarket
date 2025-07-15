from fastapi import FastAPI
from api.user_api import router as user_router
from api.auth_api import router as auth_router


app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)