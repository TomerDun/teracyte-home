def validate_metadata(metadata):
    """
    Validate image metadata based on the ImageData model requirements.
    
    Args:
        metadata (dict): Dictionary containing image metadata fields
        
    Returns:
        bool: True if valid, False if invalid (prints error)
    """
    # Required fields
    if not metadata.get('image_id'):
        print('❌ metadata validation error: missing image_id')
        return False
    if not metadata.get('intensity_average' or float(metadata.get('intensity_average')) < 0):
        print('❌ metadata validation error: invalido rmissing intensity_average')
        return False
    if not metadata.get('focus_score'):
        print('❌ metadata validation error: missing focus_score')
        return False
    if not metadata.get('classification_label'):
        print('❌ metadata validation error: missing classification_label')
        return False
    
    print('--✔ metadata validated succesfully--', flush=True)
    return True
    