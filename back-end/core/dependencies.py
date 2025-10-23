from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from database import get_db
from core.security import decode_access_token
from models.user import User
from services.token_manager import refresh_token_if_expired

# HTTP Bearer token scheme
security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency to get current authenticated user from JWT token.
    this will also refresh the user's TC access_token if needed
    
    Args:
        credentials: HTTP Bearer token credentials
        db: Database session
        
    Returns:
        User object from database
        
    Raises:
        HTTPException: If token is invalid or user not found
    """
    token = credentials.credentials
    print('--get_current_user token: ', token, flush=True)
    
    # Decode the JWT token
    payload = decode_access_token(token)
    
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Extract username from payload
    username: str = payload.get("username")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Get user from database
    user = db.query(User).filter(User.username == username).first()
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    print('--checking if user needs TC token refresh--', flush=True)
    
    # refresh_token_if_expired handles the case where expires_at is None
    token_data = refresh_token_if_expired(
        user.tc_access_token, 
        user.tc_refresh_token,
        user.tc_access_token_expires
    )
    
    # Update token and expiration if they changed
    if token_data["access_token"] != user.tc_access_token:
        user.tc_access_token = token_data["access_token"]
        user.tc_access_token_expires = token_data["expires_at"]
        db.add(user)
        db.commit()
        db.refresh(user)
    
    
    return user
