"""
Auth Controller - Business logic for authentication
"""
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.user import User
from core.security import verify_password, create_access_token, decode_access_token
from services.tc_auth import get_tc_creds, refresh_tc_token


def login_user(username: str, password: str, db: Session) -> dict:
    """
    Authenticate user and return JWT access token
    
    Args:
        username: User's username
        password: Plain text password
        db: Database session
        
    Returns:
        Dictionary with access_token and token_type
        
    Raises:
        HTTPException: If credentials are invalid
    """
    # Find user by username
    user = db.query(User).filter(User.username == username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    # Verify password
    if not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
        
    update_user_tc_creds(user, db)
    
    # Create JWT access token
    access_token = create_access_token(data={"username": user.username})
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


def update_user_tc_creds(user: User, db: Session):
    """
    Check if user has a refresh token and if not fetch a new one.
    
    Args:
        user: User object from database
        db: Database session
    """
    
    print('--checking TC API credentials for user', user.username)
        
    if not user.tc_refresh_token:        
        print(f'--No TC refresh token found for user {user.username}, fetching new credentials--')
        tc_creds = get_tc_creds()
        user.tc_acc_token = tc_creds["access_token"]
        user.tc_refresh_token = tc_creds["refresh_token"]
        print('--TC credentials updated--')