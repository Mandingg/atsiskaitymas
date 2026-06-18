from app.services.db_connection import DatabaseManager
from app.models.category import (
    CategoryModel,
    CategoryCreateModel,
    CategoryUpdateModel,
)


class CategoryService:

    def __init__(self):
        self.db = DatabaseManager()

    def get_all_categories(self):
        categories = self.db.fetch_all(
            """
            SELECT *
            FROM categories
            ORDER BY name ASC
            """
        )

        return [CategoryModel(**category) for category in categories]

    def create_category(self, category: CategoryCreateModel):
        name = category.name.strip()

        if not name:
            raise ValueError("Kategorijos pavadinimas negali būti tuščias.")

        existing_category = self.db.fetch_one(
            """
            SELECT *
            FROM categories
            WHERE LOWER(name) = LOWER(%s)
            """,
            (name,)
        )

        if existing_category:
            raise ValueError("Tokia kategorija jau egzistuoja.")

        category_id = self.db.insert(
            """
            INSERT INTO categories (name)
            VALUES (%s)
            """,
            (name,)
        )

        return category_id

    def update_category(self, category_id: int, category: CategoryUpdateModel):
        existing_category = self.db.fetch_one(
            """
            SELECT *
            FROM categories
            WHERE id = %s
            """,
            (category_id,)
        )

        if not existing_category:
            raise ValueError("Kategorija nerasta.")

        if category.name is None:
            raise ValueError("Nėra ką atnaujinti.")

        name = category.name.strip()

        if not name:
            raise ValueError("Kategorijos pavadinimas negali būti tuščias.")

        duplicate_category = self.db.fetch_one(
            """
            SELECT *
            FROM categories
            WHERE LOWER(name) = LOWER(%s)
            AND id != %s
            """,
            (name, category_id)
        )

        if duplicate_category:
            raise ValueError("Tokia kategorija jau egzistuoja.")

        updated_rows = self.db.update(
            """
            UPDATE categories
            SET name = %s
            WHERE id = %s
            """,
            (name, category_id)
        )

        if updated_rows == 0:
            raise ValueError("Nepavyko atnaujinti kategorijos.")

    def delete_category(self, category_id: int):
        existing_category = self.db.fetch_one(
            """
            SELECT *
            FROM categories
            WHERE id = %s
            """,
            (category_id,)
        )

        if not existing_category:
            raise ValueError("Kategorija nerasta.")

        deleted_rows = self.db.delete(
            """
            DELETE FROM categories
            WHERE id = %s
            """,
            (category_id,)
        )

        if deleted_rows == 0:
            raise ValueError("Nepavyko ištrinti kategorijos.")