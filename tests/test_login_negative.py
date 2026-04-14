import pytest
from pages.login_page import LoginPage
from data.test_data import INVALID_LOGIN_CASES

@pytest.mark.parametrize(
    "username, password, expected_error",
    INVALID_LOGIN_CASES
)

def test_invalid_login(page, username, password, expected_error):
    login_page = LoginPage(page)

    login_page.open()

    login_page.login(username, password)

    login_page.wait_for_error()
    
    assert expected_error in login_page.get_error_text()