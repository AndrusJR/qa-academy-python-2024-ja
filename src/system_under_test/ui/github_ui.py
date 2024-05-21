# from src.system_under_test.ui.pages.signup_page import SignUpPage
from src.system_under_test.ui.base_app import BaseApp
from src.system_under_test.ui.pages.login_page import LoginPage


class GitHubUI(BaseApp):

    def __init__(self, browser) -> None:
        super().__init__(browser)

        self.login_page = LoginPage(self)

    def open(self):
        self.open_browser()

    def try_login(self, username: str, password: str):
        return self.login_page.try_login(username, password)

    def check_wrong_creds_message(self, message: str):
        return self.login_page.check_wrong_creds_message(message)

    def logout(self):
        self.wait_and_click(locators, timer)

    def create_user(self):
        pass

    def close(self):
        self.close_browser()
