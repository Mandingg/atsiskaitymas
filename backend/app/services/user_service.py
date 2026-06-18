from app.services.db_connection import DatabaseManager
from app.models.user import UserCreateModel


class UserService:

    def __init__(self):
        self.db = DatabaseManager()

    def get_user_by_email(self, email: str):
        query = "SELECT * FROM users WHERE email = %s"
        return self.db.fetch_one(query, (email,))

    def get_user_by_id(self, user_id: int):
        query = "SELECT * FROM users WHERE id = %s"
        return self.db.fetch_one(query, (user_id,))

    def create_user(self, user: UserCreateModel, password_hash: str):
        query = """
            INSERT INTO users (name, surname, email, password_hash, role)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            user.name,
            user.surname,
            user.email,
            password_hash,
            "USER",
        )

        return self.db.insert(query, values)
