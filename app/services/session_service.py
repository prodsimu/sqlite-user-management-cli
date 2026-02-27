from app.repositories.session_repository import SessionRepository
from app.domain.session import Session


class SessionService:

    def __init__(self, session_repository: SessionRepository) -> None:
        self.session_repository: SessionRepository = session_repository
