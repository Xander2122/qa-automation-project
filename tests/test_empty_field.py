import pytest
from pages.login_page import LoginPage
from data.test_data import EMPTY_FIELD_CASES

@pytest.mark.parametrize(
    "username, password, expected_error",
    EMPTY_FIELD_CASES
)

def test_field(page, username, password, expected_error):
    login_page = LoginPage(page)
    
    login_page.open()
    login_page.login(username, password)
    
    #assert "practice-test-login" in page.url
    
    login_page.wait_for_error()
    assert expected_error in login_page.get_error_text()