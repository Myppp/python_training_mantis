def test_login(app):
    app.session.login("administrator", "aFwzAyeeeJHJE5@")
    assert app.session.is_logged_in_as("administrator ( Дмитрий )")