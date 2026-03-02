from app.database.migrations import create_tables
from app.services.user_service import UserService
from app.services.session_service import SessionService
from app.repositories.user_repository import UserRepository
from app.repositories.session_repository import SessionRepository
from app.controllers.app_controller import AppController
from app.ui.cli import CLI


def build_app() -> CLI:
    user_repository = UserRepository()
    session_repository = SessionRepository()
    user_service = UserService(user_repository)
    session_service = SessionService(session_repository)
    app_controller = AppController(user_service, session_service)

    return CLI(app_controller)


def start():
    create_tables()
    cli = build_app()
    cli.start_app()


if __name__ == "__main__":
    start()
