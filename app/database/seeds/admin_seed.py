from app.services.user_service import UserService


def admin_seed(user_service: UserService):
    existing_admin = user_service.user_repository.find_by_username("admin")

    if existing_admin:
        return False

    user_service.create_admin("Admin", "admin", "admin123")

    return True
