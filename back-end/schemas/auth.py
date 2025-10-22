"""
Pydantic schemas for Authentication
"""
from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    """Login request schema"""
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")


class LoginResponse(BaseModel):
    """Login response schema"""
    access_token: str
    token_type: str
