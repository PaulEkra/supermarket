from datetime import timedelta
import jwt
import os
from datetime import datetime, timezone


def create_refresh_token(data: dict, expires_delta: timedelta = timedelta(days=int(os.getenv("REFRESH_TOKEN_EXPIRE_TIME")))) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt