from fastapi import FastAPI, Header, HTTPException
from config import settings
from security import create_token, verify_token 

def get_api_key(api_key: str = Header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
        
def get_current_user(token: str = Header(...)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid JWT Token")
    return payload