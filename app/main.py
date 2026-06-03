from fastapi import FastAPI
from app.core.config import env_settings
from models.users import AuthObject

app = FastAPI()

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": env_settings.APP_NAME,
        "version": env_settings.VERSION
    }

@app.post("/auth")
async def auth(user:AuthObject):
    pass
