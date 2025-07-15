from sqlmodel import SQLModel
from datetime import datetime

class AccessTokenSchema(SQLModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_at: datetime
    