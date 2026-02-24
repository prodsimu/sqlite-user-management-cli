from datetime import datetime
from app.database.connection import DatabaseConnection
from app.models.session import Session


class SessionRepository:
    def __init__(self):
        self.connection = DatabaseConnection().get_connection()

    def create(self, user_id: int) -> Session:
        created_at = datetime.utcnow().isoformat()

        cursor = self.connection.execute(
            """
            INSERT INTO sessions (user_id, created_at)
            VALUES (?, ?)
            """,
            (user_id, created_at),
        )
        self.connection.commit()

        session_id = cursor.lastrowid
        return Session(session_id, user_id, created_at)
