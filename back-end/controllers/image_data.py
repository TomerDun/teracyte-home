"""
ImageData Controller - Business logic for image data
"""
from sqlalchemy.orm import Session
from models.user import User
from models.image_data import ImageData
from services.tc_image_data import fetch_image_metadata, fetch_image_file
import base64
import os

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
    print('ct metadata: ', latest_ct_metadata, flush=True)
    latest_db_img = db.query(ImageData).order_by(ImageData.created_at.desc()).first()
            
    if latest_ct_metadata['image_id'] == latest_db_img.tc_image_id:
        return False

    # New image found
    print('--new image_id found, fetching image file--')
    new_tc_image_data = fetch_image_file(user.tc_access_token)
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
        classification_label=latest_ct_metadata['classification_label']
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