class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def wait_for_url(self, url):
        self.page.wait_for_url(url)

    def get_title(self):
        return self.page.title()