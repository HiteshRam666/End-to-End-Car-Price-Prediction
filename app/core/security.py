from datetime import datetime, timezone, timedelta
from jose import jwt, JWTError
from app.core.config import settings

# Creating token
def create_token(data: dict, expire_minutes = 30):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
    to_encode.update({'exp': expire})
    return jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY, 
        algorithm=settings.JWT_ALGORITHM
    )

# Verify the given token 
def verify_token(token: str):
    try:
        payload = jwt.decode(
            token, 
            settings.JWT_SECRET_KEY, 
            algorithms=settings.JWT_ALGORITHM
        )
        return payload
    except JWTError:
        None