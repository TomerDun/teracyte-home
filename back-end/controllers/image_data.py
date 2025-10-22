"""
ImageData Controller - Business logic for image data
"""
from sqlalchemy.orm import Session
from models.user import User


def check_new_images(user: User, db: Session):
    """
    Check for new images from TC API
    
    Args:
        user: Authenticated user
        db: Database session
        
    Returns:
        Response with new images data
    """
    # TODO: Implement logic to check for new images
    pass
