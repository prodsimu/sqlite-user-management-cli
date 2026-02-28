from app.controllers.app_controller import AppController
from app.domain.user_role import UserRole


class CLI:
    def __init__(self, controller: AppController):
        self.controller = controller

    # MAIN LOOP

    def main_loop(self) -> None:
        while self.running:

            if not self.current_session:
                pass

            if self.current_user.role == UserRole.USER.value:
                pass

            if self.current_user.role == UserRole.ADMIN.value:
                pass
