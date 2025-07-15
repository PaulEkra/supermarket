from datetime import timedelta
from typing import Tuple
import jwt
import os
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()


def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=int(os.getenv("ACCESS_TOKEN_EXPIRE_TIME")))) -> Tuple[str, datetime]:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt, expire