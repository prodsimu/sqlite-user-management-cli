import sqlite3
from pathlib import Path

DB_PATH = Path("database.db")


class DatabaseConnection:
    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.connection.execute("PRAGMA foreign_keys = ON;")
        self.connection.row_factory = sqlite3.Row

    def get_connection(self):
        return self.connection
