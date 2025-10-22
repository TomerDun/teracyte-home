"""
ImageData Router - Image data endpoints
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from core.dependencies import get_current_user
from models.user import User
from controllers.image_data import check_new_images


# Create image_data router
router = APIRouter(
    prefix="/images",
    tags=["Images"]
)


@router.get("/check-new")
async def check_new(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Check for new images from TC API (Protected endpoint)
    
    Requires authentication via JWT token in Authorization header.
    
    Args:
        current_user: Authenticated user (from JWT token)
        db: Database session
        
    Returns:
        New images data
    """
    result = check_new_images(user=current_user, db=db)
    
    return result
