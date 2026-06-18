from mysql import connector
from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseManager:

    def __init__(self):
        self.host = os.getenv("MYSQL_HOST")
        self.user = os.getenv("MYSQL_USER")
        self.password = os.getenv("MYSQL_PASSWORD")
        self.database = os.getenv("MYSQL_DATABASE")
        self.port = int(os.getenv("MYSQL_PORT", 3306))

    def _connect(self):
        return connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

    def fetch_all(self, query, params=None):
        connection = self._connect()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(query, params)
            return cursor.fetchall()

        except connector.Error as error:
            print(f"Klaida vykdant query: {error}")
            return []

        finally:
            cursor.close()
            connection.close()

    def fetch_one(self, query, params=None):
        connection = self._connect()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(query, params)
            return cursor.fetchone()

        except connector.Error as error:
            print(f"Klaida vykdant query: {error}")
            return None

        finally:
            cursor.close()
            connection.close()

    def insert(self, query, params=None):
        connection = self._connect()
        cursor = connection.cursor()

        try:
            cursor.execute(query, params)
            connection.commit()
            return cursor.lastrowid

        except connector.Error as error:
            print(f"Klaida vykdant query: {error}")
            connection.rollback()
            return None

        finally:
            cursor.close()
            connection.close()

    def update(self, query, params=None):
        connection = self._connect()
        cursor = connection.cursor()

        try:
            cursor.execute(query, params)
            connection.commit()
            return cursor.rowcount

        except connector.Error as error:
            print(f"Klaida vykdant query: {error}")
            connection.rollback()
            return 0

        finally:
            cursor.close()
            connection.close()

    def delete(self, query, params=None):
        connection = self._connect()
        cursor = connection.cursor()

        try:
            cursor.execute(query, params)
            connection.commit()
            return cursor.rowcount

        except connector.Error as error:
            print(f"Klaida vykdant query: {error}")
            connection.rollback()
            return 0

        finally:
            cursor.close()
            connection.close()