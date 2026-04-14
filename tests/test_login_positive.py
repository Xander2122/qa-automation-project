from pages.login_page import LoginPage

def test_successful_login_and_logout(page):
    login_page = LoginPage(page)
    login_page.open()
    assert "Test Login | Practice Test Automation" in page.title()
    
    login_page.login("student", "Password123")
    
    login_page.wait_for_success_url()
    assert page.url == LoginPage.SUCCESS_URL
    assert login_page.get_title_text() == "Logged In Successfully"
    assert login_page.get_success_text() == "Congratulations student. You successfully logged in!"
    assert login_page.is_logout_visible()
    
    login_page.click_logout()
    page.wait_for_url(LoginPage.URL)
    assert page.url == LoginPage.URL
