from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
)
from app.modules.auth.models import User
from app.modules.auth.repository import UserRepository
from app.modules.auth.schemas.requests import (
    UserLoginRequest,
    UserRegisterRequest,
)


class AuthService:

    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(
        self,
        db: Session,
        data: UserRegisterRequest
    ) -> User:

        existing_user = self.user_repository.get_by_email(
            db,
            data.email
        )

        if existing_user:
            raise ValueError("Email already registered")

        user = User(
            full_name=data.full_name,
            email=data.email,
            phone=data.phone,
            password_hash=hash_password(data.password),
            role="tenant",
            is_active=True
        )

        return self.user_repository.create(db, user)

    def login_user(
        self,
        db: Session,
        data: UserLoginRequest
    ) -> dict:

        user = self.user_repository.get_by_email(
            db,
            data.email
        )

        if not user:
            raise ValueError("Invalid email or password")

        if not user.is_active:
            raise ValueError("User account is inactive")

        if not verify_password(
            data.password,
            user.password_hash
        ):
            raise ValueError("Invalid email or password")

        access_token = create_access_token(
            str(user.id)
        )

        refresh_token = create_refresh_token(
            str(user.id)
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }

    def refresh_access_token(
        self,
        db: Session,
        refresh_token: str
    ) -> dict:

        payload = decode_token(refresh_token)

        if payload.get("type") != "refresh":
            raise ValueError("Invalid refresh token")

        user_id = payload.get("sub")

        if not user_id:
            raise ValueError("Invalid refresh token")

        user = self.user_repository.get_by_id(
            db,
            user_id
        )

        if not user:
            raise ValueError("User not found")

        if not user.is_active:
            raise ValueError("User account is inactive")

        access_token = create_access_token(
            str(user.id)
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }