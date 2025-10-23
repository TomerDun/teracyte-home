from jose import jwt, JWTError


def refresh_token_if_expired(access_token: str, refresh_token: str):
    """
    Refresh the access token if it has expired.
    
    Args:
        access_token: Current access token
        refresh_token: Refresh token
    Returns:
        New access token if refreshed, else the original access token
    """

def verify_token_format(token: str) -> bool:
    print(token, flush=True)
    """
    Verify if the token matches the expected JWT schema structure.    
    
    Args:
        token: Token string to verify
    Returns:
        True if token matches JWT schema, False otherwise
    """
    try:
        payload = jwt.decode(
            token=token,
            key="",  # Dummy key (not used when verify_signature is False)
            options={
                "verify_signature": False,
                "verify_exp": False,  # Don't verify expiration
            }
        )           
        if not isinstance(payload, dict) or 'sub' not in payload:
            
            return False                
        
        return True
     
     
    except JWTError as e:
        print('JWTError: ', e, flush=True)
        print('JWTError encountered during token schema verification', flush=True)
        return False
    except Exception as e:        
        print('Exception: ', e, flush=True)
        print('General Exception encountered during token schema verification', flush=True)
        return False