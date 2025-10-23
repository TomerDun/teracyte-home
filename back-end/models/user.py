"""
User SQLAlchemy model
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base


class User(Base):
    """
    User model for storing user information
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    tc_access_token = Column(String(500), nullable=True)
    tc_refresh_token = Column(String(500), nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
