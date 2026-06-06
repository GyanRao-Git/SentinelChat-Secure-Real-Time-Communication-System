from pydantic import BaseModel, EmailStr, field_validator
from utils.utility import password_validator

class Credentials(BaseModel):
    username: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        val = password_validator(value=value)
        return val
        
class SignUpObject(Credentials):
    name: str
    nick_name:str
    country_code: str
    phone_number: str
    
class LoginObject(Credentials):
    pass
    

        



