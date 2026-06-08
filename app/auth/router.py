from fastapi import APIRouter
import jwt
from app.schemas.auth import SignUpObject


router = APIRouter()

@router.post("/sign-up")
async def signUp(data:SignUpObject):
    pass
    

@router.post("/login")
async def login():
    pass


