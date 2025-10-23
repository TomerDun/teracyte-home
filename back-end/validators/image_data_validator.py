from PIL import Image
import io


def validate_metadata(metadata):
    """
    Validate image metadata based on the ImageData model requirements.
    
    Args:
        metadata (dict): Dictionary containing image metadata fields
        
    Returns:
        bool: True if valid, False if invalid (prints error)
    """
    
    if not metadata.get('image_id'):
        print('❌ metadata validation error: missing image_id')
        return False
    if not metadata.get('intensity_average' or float(metadata.get('intensity_average')) < 0):
        print('❌ metadata validation error: invalid or missing intensity_average')
        return False
    if not metadata.get('focus_score'):
        print('❌ metadata validation error: missing focus_score')
        return False
    if not metadata.get('classification_label'):
        print('❌ metadata validation error: missing classification_label')
        return False
    if not metadata.get('histogram'):
        print('❌ metadata validation error: missing histogram')
        return False
    if not validate_histogram(metadata['histogram']):
        return False
    
    print('--✔ metadata validated succesfully--', flush=True)
    return True
    
def validate_histogram(histogram):
    """
    Validate histogram data.
    
    Args:
        histogram (list): List of histogram values
        
    Returns:
        bool: True if valid, False if invalid (prints error)
    """
    
    if len(histogram) != 256:
        print('❌ histogram validation error: histogram must have 256 values')
        return False

    for value in histogram:
        if value < 0:
            print('❌ histogram validation error: histogram values must be non-negative')
            return False
    
    return True


def validate_image_file(image_bytes: bytes) -> bool:
    """
    Validate that image bytes represent a valid, non-corrupt PNG file.
    Uses Pillow to verify image integrity.
    
    Args:
        image_bytes: Raw image bytes (already decoded from base64)
    
    Returns:
        bool: True if valid, False if corrupt
    """
    try:
        # Try to open the image
        img = Image.open(io.BytesIO(image_bytes))
        
        # Verify file integrity (checks for corruption)
        img.verify()
        
        print('--✔ image file validated successfully--', flush=True)
        return True
        
    except Exception as e:
        print(f'❌ image validation error: {e}', flush=True)
        return False