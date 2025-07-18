import jwt
import os
from fastapi import HTTPException, status
from fastapi import Depends
from sqlmodel import Session, select
from users.models import UserModel
from users.schemas.token.acces_token_schema import AccessTokenSchema
from utils import get_session
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
        token_data = AccessTokenSchema(username=username)
    except jwt.JWTError:
        raise credentials_exception
    db_user = session.exec(select(UserModel).where(UserModel.username == token_data.username)).first()
    if db_user is None:
        raise credentials_exception
    return db_user