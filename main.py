from app.database.migrations import create_tables


def start():
    create_tables()
    print("System initialized successfully.")


if __name__ == "__main__":
    start()
