class Menu:

    @staticmethod
    def public_menu() -> None:
        print("1 - Login")
        print("0 - Shutdown")

    @staticmethod
    def admin_menu() -> None:
        print("=== ADMIN MENU ===")
        print("1 - Create user")
        print("2 - List users")
        print("3 - Update user")
        print("4 - Delete user")
        print("0 - Logout")
