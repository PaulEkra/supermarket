from sqlalchemy import Column, String, Boolean
from sqlmodel import Field
from base.helpers import DateTimeModel

class UserModel(DateTimeModel, table=True):
    username: str = Field(sa_column=Column(String(50), unique=True, nullable=False))
    hashed_password: str = Field(sa_column=Column(String, nullable=False))
    email: str = Field(sa_column=Column(String(50), unique=True, nullable=False))
    first_name: str = Field(sa_column=Column(String(50), nullable=True))
    last_name: str = Field(sa_column=Column(String(100), nullable=True))
    is_active: bool = Field(default=False)
