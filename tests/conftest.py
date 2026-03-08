import sqlite3

import pytest

from app.repositories.session_repository import SessionRepository
from app.repositories.user_repository import UserRepository
from app.services.session_service import SessionService
from app.services.user_service import UserService


@pytest.fixture
def test_db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")

    conn.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        );
    """
    )

    conn.execute(
        """
        CREATE TABLE sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            active INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
    """
    )

    yield conn

    conn.close()


@pytest.fixture
def user_repository(test_db):
    return UserRepository(test_db)


@pytest.fixture
def session_repository(test_db):
    return SessionRepository(test_db)


@pytest.fixture
def user_service(user_repository):
    return UserService(user_repository)


@pytest.fixture
def session_service(session_repository):
    return SessionService(session_repository)
