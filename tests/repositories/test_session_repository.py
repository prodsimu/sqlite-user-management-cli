from app.domain.session_active import SessionActive


def test_session_repository_create(user_repository, session_repository):
    user = user_repository.create("ignatius", "ignatius123", "hashed_password", "user")

    session = session_repository.create(user.id)

    assert session.id == 1
    assert session.user_id == 1
    assert session.active == SessionActive.ACTIVE.value
