from app.services.db_connection import DatabaseManager
from app.models.book import (
    BookModel,
    BookCreateModel,
    BookUpdateModel,
)


class BookService:

    def __init__(self):
        self.db = DatabaseManager()

    def get_all_books(self, category: str | None = None, sort: str = "desc"):

        query = """
        SELECT *
        FROM books
        """

        params = []

        if category:
            query += " WHERE category = %s"
            params.append(category)

        if sort == "asc":
            query += " ORDER BY rating ASC"
        else:
            query += " ORDER BY rating DESC"

        books = self.db.fetch_all(query, tuple(params))

        return [BookModel(**book) for book in books]

    def get_book_by_id(self, book_id: int):

        book = self.db.fetch_one(
            """
            SELECT *
            FROM books
            WHERE id = %s
            """,
            (book_id,)
        )

        if not book:
            raise ValueError("Knyga nerasta.")

        return BookModel(**book)

    def create_book(self, book: BookCreateModel, user_id: int):

        title = book.title.strip()
        author = book.author.strip()
        category = book.category.strip()

        if not title:
            raise ValueError("Knygos pavadinimas negali būti tuščias.")

        if not author:
            raise ValueError("Autorius negali būti tuščias.")

        if not category:
            raise ValueError("Kategorija negali būti tuščia.")
        
        existing_category = self.db.fetch_one(
        """
        SELECT *
        FROM categories
        WHERE LOWER(name) = LOWER(%s)
        """,
        (category,)
    )

        if not existing_category:
            raise ValueError("Tokios kategorijos nėra.")
        

        book_id = self.db.insert(
            """
            INSERT INTO books
            (
                user_id,
                title,
                author,
                category,
                rating,
                description
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                user_id,
                title,
                author,
                category,
                book.rating,
                book.description,
            )
        )

        return book_id

    def update_book(self, book_id: int, book: BookUpdateModel, user_id: int, role: str):

        existing_book = self.db.fetch_one(
            """
            SELECT *
            FROM books
            WHERE id = %s
            """,
            (book_id,)
        )

        if not existing_book:
            raise ValueError("Knyga nerasta.")

        if role != "ADMIN" and existing_book["user_id"] != user_id:
            raise ValueError("Negalite redaguoti kito vartotojo knygos.")

        update_fields = {}

        if book.title is not None:
            title = book.title.strip()

            if not title:
                raise ValueError("Knygos pavadinimas negali būti tuščias.")

            update_fields["title"] = title

        if book.author is not None:
            author = book.author.strip()

            if not author:
                raise ValueError("Autorius negali būti tuščias.")

            update_fields["author"] = author

        if book.category is not None:
            category = book.category.strip()

            if not category:
                raise ValueError("Kategorija negali būti tuščia.")

            update_fields["category"] = category

        if book.rating is not None:
            update_fields["rating"] = book.rating

        if book.description is not None:
            update_fields["description"] = book.description

        if not update_fields:
            raise ValueError("Nėra ką atnaujinti.")

        set_clause = ", ".join([f"{field} = %s" for field in update_fields])
        values = list(update_fields.values())
        values.append(book_id)

        updated_rows = self.db.update(
            f"""
            UPDATE books
            SET {set_clause}
            WHERE id = %s
            """,
            tuple(values)
        )

        if updated_rows == 0:
            raise ValueError("Nepavyko atnaujinti knygos.")

    def delete_book(self, book_id: int, user_id: int, role: str):

        existing_book = self.db.fetch_one(
            """
            SELECT *
            FROM books
            WHERE id = %s
            """,
            (book_id,)
        )

        if not existing_book:
            raise ValueError("Knyga nerasta.")

        if role != "ADMIN" and existing_book["user_id"] != user_id:
            raise ValueError("Negalite ištrinti kito vartotojo knygos.")

        deleted_rows = self.db.delete(
            """
            DELETE FROM books
            WHERE id = %s
            """,
            (book_id,)
        )

        if deleted_rows == 0:
            raise ValueError("Nepavyko ištrinti knygos.")