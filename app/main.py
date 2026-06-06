from fastapi import FastAPI
from app.core.config import app_settings,db_settings
from app.auth.router import router as auth_router

app = FastAPI()

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": app_settings.APP_NAME,
        "version": app_settings.VERSION
    }

app.include_router(auth_router, prefix="/auth")
