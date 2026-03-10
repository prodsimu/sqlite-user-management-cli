from app.domain.session_active import SessionActive


def test_session_service_create_session_new_user(user_service, session_service):
    user = user_service.create("Test User", "testuser", "password123")

    session = session_service.create_session(user.id)

    assert session.id is not None
    assert session.user_id == user.id
    assert session.active == SessionActive.ACTIVE.value
    assert session.created_at is not None


def test_session_service_create_session_existing_active(user_service, session_service):
    user = user_service.create("Test User", "testuser", "password123")

    first_session = session_service.create_session(user.id)
    assert first_session.active == SessionActive.ACTIVE.value

    second_session = session_service.create_session(user.id)

    active_session = session_service.session_repository.get_active_by_user(user.id)
    assert active_session is not None
    assert active_session.id == second_session.id
    assert active_session.active == SessionActive.ACTIVE.value
