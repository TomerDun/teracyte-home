"""
ImageData Controller - Business logic for image data
"""
from sqlalchemy.orm import Session
from models.user import User
from models.image_data import ImageData
from services.tc_image_data import fetch_image_metadata, fetch_image_file
import base64
import os
from validators.image_data_validator import validate_metadata

def check_new_images(user: User, db: Session):
    """
    retrieves new image metadata and compares against the latest in the DB. updates with new image data and new image if needed.
    
    Args:
        user: Authenticated user
        db: Database session
        
    Returns:
        Response with new images data
    """
    
    latest_ct_metadata = fetch_image_metadata(user.tc_access_token, user.tc_refresh_token)        
    if not validate_metadata(latest_ct_metadata):
        return False
    
    # print('ct metadata: ', latest_ct_metadata, flush=True)
    latest_db_img = db.query(ImageData).order_by(ImageData.created_at.desc()).first()
            
    if latest_ct_metadata['image_id'] == latest_db_img.tc_image_id:
        return False

    # New image found
    
    print('--new image_id found, fetching image file--')
    new_tc_image_data = fetch_image_file(user.tc_access_token)
    
    if new_tc_image_data['image_id'] != latest_ct_metadata['image_id']:
        print('❌ image_id mismatch between metadata and image file response')
        return False
    
    new_tc_image_file = new_tc_image_data['image_data_base64']
    # print('new_tc_image: ', new_tc_image_file, flush=True)    
    
    # Save image to filesystem    
    filename = f"{latest_ct_metadata['image_id']}.png"    
    static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "cell_images", "raw")    
    os.makedirs(static_dir, exist_ok=True) # Ensure directory exists
    file_path = os.path.join(static_dir, filename)
    
    relative_path = f"/static/cell_images/raw/{filename}" 
    
    # Write image bytes to file    
    image_bytes = base64.b64decode(new_tc_image_file)        
    
    with open(file_path, "wb") as f:
        f.write(image_bytes)
    
    print(f'--Image saved to: {file_path}--')
    
    # Store new image data in database
    new_image_data = ImageData(
        tc_image_id=latest_ct_metadata['image_id'],
        raw_image_path=relative_path,
        intensity_average=latest_ct_metadata['intensity_average'],
        focus_score=latest_ct_metadata['focus_score'],
        classification_label=latest_ct_metadata['classification_label'],
        histogram=latest_ct_metadata.get('histogram'),
    )
    
    db.add(new_image_data)
    db.commit()
    db.refresh(new_image_data)
    
    print(f'--New image data saved to database with ID: {new_image_data.id}--')
    
    return {
        "status": "success",        
        "image": new_image_data
    }


def get_latest_image_data(db: Session):
    """
    Retrieve the latest image data from the database.
    
    Args:
        db: Database session
    Returns:
        Latest ImageData object or None if no data exists
    """
    return db.query(ImageData).order_by(ImageData.created_at.desc()).first()


def get_image_data_history(db: Session):
    """
    Retrieve image data history with selected fields only.
    
    Args:
        db: Database session
    Returns:
        List of dictionaries containing tc_image_id, classification_label, and created_at
        sorted by created_at from newest to oldest
    """
    results = db.query(
        ImageData.tc_image_id,
        ImageData.classification_label,
        ImageData.created_at
    ).order_by(ImageData.created_at.desc()).all()
    
    return [
        {
            "tc_image_id": result.tc_image_id,
            "classification_label": result.classification_label,
            "created_at": result.created_at
        }
        for result in results
    ]