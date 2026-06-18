from passlib.context import CryptContext
from fastapi import HTTPException, status

from app.models.user import UserCreateModel, UserLoginModel
from app.services.user_service import UserService
from app.auth.jwt_handler import create_token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:

    def __init__(self):
        self.user_service = UserService()

    def register(self, user: UserCreateModel):
        existing_user = self.user_service.get_user_by_email(user.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Toks el. paštas jau egzistuoja."
            )

        password_hash = self.hash_password(user.password)

        user_id = self.user_service.create_user(user, password_hash)
       
        return {
            "id": user_id,
            "name": user.name,
            "surname": user.surname,
            "email": user.email,
            "role": "USER",
            "message": "Paskyra sukurta sėkmingai."
        }

    def login(self, user: UserLoginModel):
        existing_user = self.user_service.get_user_by_email(user.email)

        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Neteisingas el. paštas arba slaptažodis."
            )

        if not self.verify_password(
            user.password,
            existing_user["password_hash"]
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Neteisingas el. paštas arba slaptažodis."
            )

        token = create_token({
            "sub": str(existing_user["id"]),
            "role": existing_user["role"],
        })

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)