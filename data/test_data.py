VALID_USERNAME = "student"
VALID_PASSWORD = "Password123"

INVALID_USERNAME = "incorrectUser"
INVALID_PASSWORD = "wrongPassword"

INVALID_LOGIN_CASES = [
    ("student", "wrongPassword", "Your password is invalid!"),
    ("incorrectUser", "Password123", "Your username is invalid!"),
]

EMPTY_FIELD_CASES = [
    ("", "Password123", "Your username is invalid!"),
    ("student", "", "Your password is invalid!"),
    ("", "", "Your username is invalid!"),
]