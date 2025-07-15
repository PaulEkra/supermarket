from sqlmodel import SQLModel

class RefreshTokenResponseSchema(SQLModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_at: str