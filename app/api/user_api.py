from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from utils.get_current_user import get_current_user
from utils.hash_password import hash_password
from users.schemas.user.user_create_response import UserResponseSchema
from utils.get_session import get_session
from users.schemas.user.user_create_schema import UserCreateSchema
from users.models.user_model import UserModel as User
from utils.get_current_user import oauth2_scheme

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@router.post("/signin", response_model=UserResponseSchema)
def create_user(user: UserCreateSchema, session: Session = Depends(get_session)):
    
   
    db_user = session.exec(select(User).where(User.username == user.username)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    db_user = session.exec(select(User).where(User.email == user.email)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hacher le mot de passe
    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password, email=user.email)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    
    return db_user



@router.get("/me", response_model=UserResponseSchema)
def get_profil(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    user = get_current_user(token, session)
    return user