from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from auth import decode_token
from database import get_db
from models import User
oauth2_scheme=OAuth2PasswordBearer(
    tokenUrl='login'
)
async def get_current_user(
    token:str=Depends(oauth2_scheme),
    db:Session=Depends(get_db)
):
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid or expired token',
        headers={
            'WWW-Authenticate':'Bearer'
        }
    )
    try:
        payload=decode_token(token)
        username=payload.get('sub')
        token_type=payload.get('type')
        if username is None:
            raise credentials_exception
        if token_type!='access':
            raise credentials_exception
    except Exception:
        raise credentials_exception
    user=(
        db.query(User)
        .filter(User.username==username)
        .first()
    )
    if user is None:
        raise credentials_exception
    return user
def require_role(required_role:str):
    async def role_checker(
        current_user:User=Depends(get_current_user)
    ):
        if current_user.role!=require_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Insufficient permissions'
            )
        return current_user
    return role_checker