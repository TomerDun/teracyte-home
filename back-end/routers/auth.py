"""
Auth Router - Authentication endpoints
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.auth import login_user
from schemas.auth import LoginRequest, LoginResponse


# Create auth router
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login", response_model=LoginResponse)
async def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):
    """
    Login endpoint - Authenticate user and return JWT token
    
    Args:
        credentials: Username and password
        db: Database session
        
    Returns:
        JWT access token and token type
    """
    result = login_user(
        username=credentials.username,
        password=credentials.password,
        db=db
    )
    
    return result
