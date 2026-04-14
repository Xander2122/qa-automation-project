from pages.base_page import BasePage

class LoginPage(BasePage):
    
    URL = "https://practicetestautomation.com/practice-test-login/"
    SUCCESS_URL = "https://practicetestautomation.com/logged-in-successfully/"
    
    def __init__(self, page):
        super().__init__(page)
        
        self.page = page
        #self.url = "https://practicetestautomation.com/practice-test-login/"
        
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.button_submit = page.get_by_role("button", name = "Submit")
        self.error_message = page.locator("#error")
        self.logout_link = page.get_by_role("link", name="Log out")
        self.success_message = page.locator("h1")
        self.success_message1 = page.locator("strong")
        
    def open(self):
        super().open(self.URL)
    
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.button_submit.click()
        
    def wait_for_success_url(self):
        self.page.wait_for_url(self.SUCCESS_URL)
    
    def wait_for_error(self):
        self.error_message.wait_for()
    
    def click_logout(self):
        self.logout_link.click()
    
    def get_error_text(self):
        return self.error_message.inner_text()

    def get_title_text(self):
        return self.success_message.inner_text()

    def get_success_text(self):
        return self.success_message1.inner_text()
    
    def is_logout_visible(self):
        return self.logout_link.is_visible()

    
    
        