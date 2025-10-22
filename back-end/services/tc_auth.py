import os
import httpx
from dotenv import load_dotenv

load_dotenv()

def get_tc_creds():
    """"
    get acces token and refresh token from TC API
    """
    print('--Retreiving TC API credentials--')
    url = os.getenv("TC_API_BASE_URL") + "/auth/login"
    username = os.getenv("TC_USERNAME")
    password = os.getenv("TC_PASSWORD")
    
    # Make POST request to get tokens
    response = httpx.post(
        url,
        json={
            "username": username,
            "password": password
        }
    )
    
    # Raise exception if request failed
    response.raise_for_status()
        
    data = response.json()
    
    return {
        "access_token": data.get("access_token"),
        "refresh_token": data.get("refresh_token")
    }

def refresh_tc_token(refresh_token: str):
    """"
    refresh access token using refresh token from TC API
    """
    
    url = os.getenv("TC_API_BASE_URL") + "/auth/refresh"
    
    print('--Refreshing TC API access token--')
    
    # Make POST request to refresh token
    response = httpx.post(
        url,
        headers={
            "Authorization": f"Bearer {refresh_token}"
        }
    )
    
    # Raise exception if request failed
    response.raise_for_status()
        
    data = response.json()
    
    return {
        "access_token": data.get("access_token"),
        "refresh_token": data.get("refresh_token")
    }