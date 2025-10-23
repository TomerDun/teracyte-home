"""
Image Storage Service - Handles filesystem storage for images
"""
import base64
import os


def decode_base64_image(image_data_base64: str) -> bytes:
    """
    Decode base64 encoded image data to bytes.
    
    Args:
        image_data_base64: Base64 encoded image data
        
    Returns:
        Decoded image bytes
    """
    return base64.b64decode(image_data_base64)


def save_image_file(image_bytes: bytes, image_id: str) -> str:
    """
    Save image bytes to filesystem and return the relative path.
    
    Args:
        image_bytes: Raw image data as bytes
        image_id: Unique identifier for the image
        
    Returns:
        Relative path to the saved image file (e.g., "/static/cell_images/raw/{image_id}.png")
    """
    # Prepare file paths
    filename = f"{image_id}.png"
    static_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), 
        "static", 
        "cell_images", 
        "raw"
    )
    os.makedirs(static_dir, exist_ok=True)
    
    file_path = os.path.join(static_dir, filename)
    relative_path = f"/static/cell_images/raw/{filename}"
    
    # Write image to file
    with open(file_path, "wb") as f:
        f.write(image_bytes)
    
    print(f'--Image saved to: {file_path}--')
    
    return relative_path
