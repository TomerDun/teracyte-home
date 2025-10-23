from datetime import datetime, timedelta
from services.tc_auth import refresh_tc_token


def refresh_token_if_expired(access_token: str, refresh_token: str, expires_at: datetime = None):
    """
    Refresh the access token if it has expired or will expire soon.
    
    Args:
        access_token: Current access token
        refresh_token: Refresh token
        expires_at: DateTime when the access token expires (None if not set yet)
    Returns:
        Dictionary with 'access_token' and 'expires_at' (new values if refreshed, original if not expired)
    """
    
    # If no expiry time is set, force a refresh to get the expiry time
    if expires_at is None:
        print('--No expiry time found, refreshing token to get expiry--', flush=True)
        tc_creds = refresh_tc_token(refresh_token)
        return {
            "access_token": tc_creds["access_token"],
            "expires_at": tc_creds["expires_at"]
        }
    
    # Check if token is expired or will expire within 5 seconds (buffer)
    current_time = datetime.utcnow()
    buffer_time = timedelta(seconds=5)
    
    if current_time < (expires_at - buffer_time):
        # Token is still valid and has more than 5 seconds left - return original
        print('--✅ Access token is valid--', flush=True)
        return {
            "access_token": access_token,
            "expires_at": expires_at
        }
    
    # Token is expired or will expire soon - refresh it
    print('--❎ Access token expired or expiring soon, refreshing--', flush=True)
    
    try:
        tc_creds = refresh_tc_token(refresh_token)
        new_access_token = tc_creds["access_token"]
        new_expires_at = tc_creds["expires_at"]
        print('--Successfully refreshed access token--', flush=True)
        return {
            "access_token": new_access_token,
            "expires_at": new_expires_at
        }
        
    except Exception as e:
        print(f'--Error refreshing token: {e}--', flush=True)
        raise