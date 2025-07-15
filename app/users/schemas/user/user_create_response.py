from sqlmodel import SQLModel
from datetime import datetime


class UserResponseSchema(SQLModel):
    id: int 
    username: str 
    email: str 
    first_name: str | None
    last_name: str | None
    created_at: datetime 
    updated_at: datetime 