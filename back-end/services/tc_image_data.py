import os
from dotenv import load_dotenv
import httpx

load_dotenv()

def get_latest_results(access_token):
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