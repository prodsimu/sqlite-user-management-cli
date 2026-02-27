from app.services.user_service import UserService
from app.database.seeds import admin_seed


class AppController:
    def __init__(self, user_service: UserService) -> None:
        self.user_service: UserService = user_service
        self.current_session = None

    def bootstrap(self) -> None:
        seed = admin_seed(self.user_service)

    def start_app(self) -> None:
        self.bootstrap()
