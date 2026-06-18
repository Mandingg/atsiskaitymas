from fastapi import APIRouter, HTTPException, status, Depends

from app.auth.dependencies import get_current_user
from app.models.category import CategoryCreateModel, CategoryUpdateModel
from app.services.category_service import CategoryService


router = APIRouter(prefix="/categories", tags=["categories"])

category_service = CategoryService()


def require_admin(payload=Depends(get_current_user)):
    try:
        if payload["role"] != "ADMIN":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Tik administratorius gali atlikti šį veiksmą."
            )

        return payload

    except HTTPException:
        raise

    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Vartotojas nerastas."
        )


@router.get("/", status_code=status.HTTP_200_OK)
def get_categories():
    try:
        return category_service.get_all_categories()

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error)
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_category(
    category: CategoryCreateModel,
    payload=Depends(require_admin)
):
    try:
        category_id = category_service.create_category(category)

        return {
            "id": category_id,
            "message": "Kategorija sukurta sėkmingai."
        }

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@router.put("/{category_id}", status_code=status.HTTP_200_OK)
def update_category(
    category_id: int,
    category: CategoryUpdateModel,
    payload=Depends(require_admin)
):
    try:
        category_service.update_category(category_id, category)

        return {
            "id": category_id,
            "message": "Kategorija atnaujinta sėkmingai."
        }

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: int,
    payload=Depends(require_admin)
):
    try:
        category_service.delete_category(category_id)

        return {
            "message": "Kategorija ištrinta sėkmingai."
        }

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )