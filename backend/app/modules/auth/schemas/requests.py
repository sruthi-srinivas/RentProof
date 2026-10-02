from pydantic import BaseModel, EmailStr, Field


class UserRegisterRequest(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: str | None = Field(default=None, max_length=20)
    password: str = Field(..., min_length=8, max_length=72)


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=72)


class RefreshTokenRequest(BaseModel):
    refresh_token: str