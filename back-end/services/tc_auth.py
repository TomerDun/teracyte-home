import os
import httpx
from datetime import datetime, timedelta
from dotenv import load_dotenv
from core.jwt_utils import verify_token_format

load_dotenv()

def get_tc_creds():
    """"
    call login on TC API to get acces token and refresh token from TC API
    """
    url = os.getenv("TC_API_BASE_URL") + "/auth/login"
    username = os.getenv("TC_USERNAME")
    password = os.getenv("TC_PASSWORD")
    
    tokens_valid = False
    retries = 0
    
    while not tokens_valid and retries < 3:        
        retries += 1
        print(f'--Retreiving TC API credentials (try: {retries})--')
        
        response = httpx.post(
            url,
            json={
                "username": username,
                "password": password
            }
        )
        
        
        response.raise_for_status()        
        data = response.json()
        
        tokens_valid = verify_token_format(data.get("access_token")) and verify_token_format(data.get("refresh_token"))
        if (tokens_valid):
            # Calculate expiration time from expires_in (seconds)
            expires_in = data.get("expires_in", 60)  # Default to 60 seconds if not provided
            expires_at = datetime.utcnow() + timedelta(seconds=expires_in)
            
            return {
                "access_token": data.get("access_token"),
                "refresh_token": data.get("refresh_token"),
                "expires_at": expires_at
            }
        else:
            print(f'--Token format verification failed, retrying--', flush=True)
    
    # If we exit the loop without returning, raise an error
    raise Exception("Failed to get TC credentials after 3 attempts - token format verification failed")


def refresh_tc_token(refresh_token: str):
    """"
    refresh access token using refresh token from TC API
    """
    
    url = os.getenv("TC_API_BASE_URL") + "/auth/refresh"
    
    retries = 0
    token_valid = False
    
    while not token_valid and retries < 3:
        retries += 1
        print(f'--Refreshing TC API access token (try: {retries})--')
            
        response = httpx.post(
            url,
            json={"refresh_token": refresh_token}
        )
        
        if response.status_code == 503:    
            print('--TC API service unavailable, retrying--', flush=True)
            continue
        
        response.raise_for_status() #Raise error for unexpected status codes     
        data = response.json()
        
        access_token = data.get("access_token")
        
        # Only verify access_token (we don't use the new refresh_token)
        token_valid = verify_token_format(access_token)
        
        if (token_valid):
            # Calculate expiration time from expires_in (seconds)
            expires_in = data.get("expires_in", 60)  # Default to 60 seconds if not provided
            expires_at = datetime.utcnow() + timedelta(seconds=expires_in)
            
            return {
                "access_token": access_token,
                "expires_at": expires_at
            }
        else:
            print(f'--Token format verification failed, retrying--', flush=True)
    
    # If we exit the loop without returning, raise an error
    raise Exception("Failed to refresh token after 3 attempts - token format verification failed")