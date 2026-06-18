from fastapi import APIRouter, Depends, HTTPException, status
from app.services.user_service import UserService
from app.auth.dependencies import get_current_user


router = APIRouter(prefix="/users", tags=["users"])

user_service = UserService()


@router.get("/me", status_code=status.HTTP_200_OK)
def get_user(payload=Depends(get_current_user)):
    user_id = int(payload.get("sub"))
    user = user_service.get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tokio vartotojo nėra."
        )

    return {
        "id": user["id"],
        "name": user["name"],
        "surname": user["surname"],
        "email": user["email"],
        "role": user["role"],
    }