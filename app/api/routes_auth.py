from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, Field
from app.core.security import create_token

router = APIRouter()

class AuthInput(BaseModel):
    username: str
    password: str

@router.post('/login')
def login(auth: AuthInput):
    if (auth.username == 'admin') and (auth.password == "admin"):
        token = create_token({'sub': auth.username})
        return {'access_token': token}

    return {'error': 'Invalid Credentials'}