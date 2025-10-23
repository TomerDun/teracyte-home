from jose import jwt, JWTError

def verify_token_format(token: str) -> bool:
    print(token, flush=True)
    """
    Verify if the token matches the expected JWT schema structure.    
    
    Args:
        token: Token string to verify
    Returns:
        True if token matches JWT schema, False otherwise
    """
    
    print(f'--checking token format for token {token}--', flush=True)
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
        print('JWTError encountered during token schema verification:', e, flush=True)
        return False
    except Exception as e:        
        print('Exception: ', e, flush=True)
        print('General Exception encountered during token schema verification: e', flush=True)
        return False