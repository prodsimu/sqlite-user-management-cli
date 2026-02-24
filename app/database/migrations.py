from app.database.connection import DatabaseConnection


def create_tables():
    conn = DatabaseConnection().get_connection()

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
    """
    )

    conn.commit()
