from pydantic import BaseModel, EmailStr, field_validator
from utils.utility import password_validator

class AuthObject(BaseModel):
    username: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        password_validator(value=value)

        



