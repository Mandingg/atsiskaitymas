from fastapi import APIRouter, status, Depends
from app.models.user import UserCreateModel, UserLoginModel, TokenResponseModel, UserResponseModel
from app.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["auth"])

auth_service = AuthService()

@router.post('/register', response_model=UserResponseModel, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreateModel):
        return auth_service.register(user)
    
    

@router.post("/login", response_model=TokenResponseModel, status_code=status.HTTP_200_OK)
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = UserLoginModel(
        email=form_data.username,
        password=form_data.password
    )
    return auth_service.login(user)