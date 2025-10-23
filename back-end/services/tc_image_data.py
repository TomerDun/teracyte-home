import os
from dotenv import load_dotenv
import httpx
from services.tc_auth import refresh_tc_token

load_dotenv()

def fetch_image_metadata(access_token, refresh_token):        
    
    """
    Fetch latest image processing results from TC API.
    
    Args:
        access_token: TC API access token
        
    Returns:
        JSON response with image processing results
    """
    
    url = os.getenv('TC_API_BASE_URL') + '/results'    
    
    
    response = httpx.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}"
        },        
    )
    
    if (response.status_code == 401):
        new_token = refresh_tc_token(refresh_token)
        access_token = new_token['access_token']
        response = httpx.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}"
        },        
    )
        
    response.raise_for_status()                
    
        
    #TODO: Error handling
        
    return response.json()

def fetch_image_file(access_token:str):
    # TODO: Add retries to make sure image_data_base64 is in the response
    """
    Fetch image file from TC API.
    
    Args:
        access_token: TC API access token
        image_id: ID of the image to fetch
    """
    
    url = os.getenv('TC_API_BASE_URL') + '/image'    
    
    response_valid = False
    retries = 0
    
    while not response_valid and retries < 3:
        retries += 1
        print(f'--Fetch image file from CT API (attempt {retries})--', flush=True)
        
        response = httpx.get(
            url,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )
        
        if (response.status_code > 500):
            print(f'--retrying on status code {response.status_code}--', flush=True)
            continue
    
        response.raise_for_status() # Raise for unexpected status codes
        try:
            res_data = response.json()
        except Exception as e:
            print(f'❌ Error parsing JSON response: {e}', flush=True)
            continue
        
        if 'image_data_base64' not in res_data:
            print(f'--retrying becuase of missing data in response--', flush=True)
            continue
        
        # TODO: Remove this flag if not needed
        response_valid = True
        
        if response_valid:    
            return res_data