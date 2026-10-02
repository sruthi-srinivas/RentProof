from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.infrastructure.database.session import get_db
from app.modules.auth.schemas.requests import UserRegisterRequest
from app.modules.auth.schemas.responses import UserResponse
from app.modules.auth.service import AuthService

from app.modules.auth.schemas.requests import (
    UserLoginRequest,
    UserRegisterRequest,
    RefreshTokenRequest,
)

from app.modules.auth.schemas.responses import (
    TokenResponse,
    UserResponse,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

auth_service = AuthService()


@router.post("/register",response_model=UserResponse,status_code=status.HTTP_201_CREATED
)
def register(
    data: UserRegisterRequest,
    db: Session = Depends(get_db)
):
    try:
        user = auth_service.register_user(db, data)
        return user

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error)
        )


@router.post("/login",response_model=TokenResponse
)
def login(
    data: UserLoginRequest,
    db: Session = Depends(get_db)
):
    try:
        return auth_service.login_user(db, data)

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error)
        )

@router.post(
    "/refresh",
    response_model=dict
)
def refresh(
    data: RefreshTokenRequest,
    db: Session = Depends(get_db)
):
    try:
        return auth_service.refresh_access_token(
            db,
            data.refresh_token
        )

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error)
        )