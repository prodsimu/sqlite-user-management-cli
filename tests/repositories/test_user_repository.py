def test_user_repository_create(user_repository):
    user = user_repository.create("ignatius", "ignatius123", "hashed_password", "user")

    assert user.id == 1
