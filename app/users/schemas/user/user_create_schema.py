from sqlmodel import SQLModel, Field
from pydantic import field_validator
import re


EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'

class UserCreateSchema(SQLModel):
    username: str = Field(max_length=50)
    password: str = Field(min_length=8)
    email: str = Field(max_length=50)

    
    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if not re.match(EMAIL_REGEX, v):
            raise ValueError("Email invalide")
        return v

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        if not re.match(PASSWORD_REGEX, v):
            raise ValueError(
                "Le mot de passe doit contenir au moins 8 caractères, une majuscule, un chiffre et un caractère spécial."
            )
        return v