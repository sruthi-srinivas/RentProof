from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.auth.models import User


class UserRepository:

    def get_by_email(
        self,
        db: Session,
        email: str
    ) -> User | None:
        result = db.execute(
            select(User).where(User.email == email)
        )

        return result.scalar_one_or_none()

    def get_by_id(
        self,
        db: Session,
        user_id: str
    ) -> User | None:
        result = db.execute(
            select(User).where(User.id == user_id)
        )

        return result.scalar_one_or_none()

    def create(
        self,
        db: Session,
        user: User
    ) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)

        return user