from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserResponse(BaseModel):
    id: str
    full_name: str
    email: str
    phone: str | None
    role: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)



class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"