from fastapi import APIRouter, HTTPException, status, Depends, Query

from app.auth.dependencies import get_current_user
from app.models.book import BookCreateModel, BookUpdateModel
from app.services.book_service import BookService


router = APIRouter(prefix="/books", tags=["books"])

book_service = BookService()


def get_logged_user(payload=Depends(get_current_user)):
    try:
        return {
            "user_id": int(payload["sub"]),
            "role": payload["role"]
        }

    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Vartotojas nerastas."
        )


@router.get("/", status_code=status.HTTP_200_OK)
def get_books(
    category: str | None = Query(default=None),
    sort: str = Query(default="desc")
):
    try:
        return book_service.get_all_books(category, sort)

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error)
        )


@router.get("/{book_id}", status_code=status.HTTP_200_OK)
def get_book(book_id: int):
    try:
        return book_service.get_book_by_id(book_id)

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_book(
    book: BookCreateModel,
    current_user=Depends(get_logged_user)
):
    try:
        book_id = book_service.create_book(
            book,
            current_user["user_id"]
        )

        return {
            "id": book_id,
            "message": "Knyga sukurta sėkmingai."
        }

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@router.put("/{book_id}", status_code=status.HTTP_200_OK)
def update_book(
    book_id: int,
    book: BookUpdateModel,
    current_user=Depends(get_logged_user)
):
    try:
        book_service.update_book(
            book_id,
            book,
            current_user["user_id"],
            current_user["role"]
        )

        return {
            "id": book_id,
            "message": "Knyga atnaujinta sėkmingai."
        }

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
    book_id: int,
    current_user=Depends(get_logged_user)
):
    try:
        book_service.delete_book(
            book_id,
            current_user["user_id"],
            current_user["role"]
        )

        return {
            "message": "Knyga ištrinta sėkmingai."
        }

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )