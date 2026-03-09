from app.domain.user_role import UserRole


def test_user_service_create(user_service):
    user = user_service.create("Ignatius", "ignatius123", "password123")

    assert user.id is not None
    assert user.name == "Ignatius"
    assert user.username == "ignatius123"
    assert user.role == UserRole.USER.value
    assert user.password != "password123"
