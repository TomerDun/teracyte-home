from jose import jwt, JWTError
from services.tc_auth import refresh_tc_token


def refresh_token_if_expired(access_token: str, refresh_token: str):
    """
    Refresh the access token if it has expired.
    
    Args:
        access_token: Current access token
        refresh_token: Refresh token
    Returns:
        New access token if refreshed, else the original access token
    """
    
    try:        
        payload = jwt.decode(
            token=access_token,
            key=None, 
            options={
                "verify_signature": False,  
                "verify_exp": True,  
            }
        )
        
        # Token is valid and not expired - return original
        print('--✅ Access token is valid--', flush=True)
        return access_token
        
    except jwt.ExpiredSignatureError:
        # Token is expired - refresh it
        print('--❎ Access token expired, refreshing--', flush=True)
        
        try:
            tc_creds = refresh_tc_token(refresh_token)
            new_access_token = tc_creds["access_token"]
            print('--Successfully refreshed access token--', flush=True)
            return new_access_token
            
        except Exception as e:
            print(f'--Error refreshing token: {e}--', flush=True)
            raise
            
    except JWTError as e:
        # Invalid token format
        print(f'--Invalid token format: {e}--', flush=True)
        raise
        
    except Exception as e:
        print(f'--Unexpected error checking token expiry: {e}--', flush=True)
        raise