"""
ImageData Router - Image data endpoints
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from core.dependencies import get_current_user
from models.user import User
import controllers.image_data as image_data_controller


# Create image_data router
router = APIRouter(
    prefix="/images",
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
    res = image_data_controller.check_new_images(user=current_user, db=db)
    
    return res

@router.get('/latest')
async def get_latest_image(current_user: User = Depends(get_current_user),
                           db: Session = Depends(get_db)):
    """
    Get the latest image data.
    
    Args:
        current_user: Authenticated user (from JWT token)
        db: Database session
    """
    
    res = image_data_controller.get_latest_image_data(db=db)
    return res


@router.get('/history')
async def get_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get image data history with tc_image_id, classification_label, and created_at.
    Returns data sorted by created_at from newest to oldest.
    
    Requires authentication via JWT token in Authorization header.
    
    Args:
        current_user: Authenticated user (from JWT token)
        db: Database session
        
    Returns:
        List of image history records
    """
    res = image_data_controller.get_image_data_history(db=db)
    return res
