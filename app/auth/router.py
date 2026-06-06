from fastapi import APIRouter
import jwt
from app.models.users import SignUpObject


router = APIRouter()

@router.post("/sign-up")
async def signUp(data:SignUpObject):
    
    

@router.post("/login")
async def login():
    pass


