"""
Pydantic schemas for User
"""
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class UserBase(BaseModel):
    """Base User schema with common attributes"""
    username: str = Field(..., min_length=3, max_length=50, description="Username (3-50 characters)")


class UserCreate(UserBase):
    """Schema for creating a new user"""
    password: str = Field(..., min_length=8, description="Password (minimum 8 characters)")


class UserResponse(UserBase):
    """Schema for user response (excludes sensitive data)"""
    id: int
    
    model_config = ConfigDict(from_attributes=True)


class UserInDB(UserBase):
    """Schema for user in database (includes hashed password and tokens)"""
    id: int
    hashed_password: str
    tc_access_token: Optional[str] = None
    tc_refresh_token: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)
