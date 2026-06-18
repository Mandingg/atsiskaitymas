import sys
import os
import pytest
from unittest.mock import MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.services.book_service import BookService
from app.models.book import BookCreateModel, BookUpdateModel


def test_create_book_fails_when_title_is_empty():
    service = BookService()

    service.db.fetch_one = MagicMock()
    service.db.insert = MagicMock()

    book = BookCreateModel(
        title="   ",
        author="Autorius",
        category="Fantasy",
        rating=5,
        description="Testinis aprašymas"
    )

    with pytest.raises(ValueError) as error:
        service.create_book(book, user_id=1)

    assert str(error.value) == "Knygos pavadinimas negali būti tuščias."
    service.db.insert.assert_not_called()


def test_user_cannot_update_other_users_book():
    service = BookService()

    service.db.fetch_one = MagicMock(return_value={
        "id": 1,
        "user_id": 99,
        "title": "Svetima knyga",
        "author": "Autorius",
        "category": "Fantasy",
        "rating": 4,
        "description": "Aprašymas",
        "created_at": "2026-06-18 10:00:00"
    })

    service.db.update = MagicMock()

    book_update = BookUpdateModel(
        rating=1
    )

    with pytest.raises(ValueError) as error:
        service.update_book(
            book_id=1,
            book=book_update,
            user_id=1,
            role="USER"
        )

    assert str(error.value) == "Negalite redaguoti kito vartotojo knygos."
    service.db.update.assert_not_called()


def test_admin_can_update_other_users_book():
    service = BookService()

    service.db.fetch_one = MagicMock(return_value={
        "id": 1,
        "user_id": 99,
        "title": "Svetima knyga",
        "author": "Autorius",
        "category": "Fantasy",
        "rating": 4,
        "description": "Aprašymas",
        "created_at": "2026-06-18 10:00:00"
    })

    service.db.update = MagicMock(return_value=1)

    book_update = BookUpdateModel(
        rating=5
    )

    service.update_book(
        book_id=1,
        book=book_update,
        user_id=1,
        role="ADMIN"
    )

    service.db.update.assert_called_once()