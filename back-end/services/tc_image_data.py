import os
from dotenv import load_dotenv
import httpx

load_dotenv()

def fetch_image_metadata(access_token):
    """
    Fetch latest image processing results from TC API.
    
    Args:
        access_token: TC API access token
        
    Returns:
        JSON response with image processing results
    """
    
    url = os.getenv('TC_API_BASE_URL') + '/results'
    
    print(f'--Fetching latest results from TC API--')
        
    response = httpx.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
        
    #TODO: Error handling
    response.raise_for_status()
        
    return response.json()

def fetch_image_file(access_token:str):
    """
    Fetch image file from TC API.
    
    Args:
        access_token: TC API access token
        image_id: ID of the image to fetch
    """
    
    url = os.getenv('TC_API_BASE_URL') + '/image/file'
    
    print(f'--Fetching image file from TC API--')
        
    response = httpx.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    
    # TODO: Error handling
    return response.json()