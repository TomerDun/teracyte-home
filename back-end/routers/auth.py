"""
Auth Router - Authentication endpoints
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.auth import login_user
from schemas.auth import LoginRequest, LoginResponse
from services.tc_auth import get_tc_creds, refresh_tc_token


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

@router.get('/tc-login')
async def get_tc_login():
    """
    TC Login endpoint - Authenticate with TC API and return tokens
    """
    
    result = get_tc_creds()

    return result