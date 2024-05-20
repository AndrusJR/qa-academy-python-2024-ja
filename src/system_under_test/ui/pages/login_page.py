from selenium.webdriver.common.by import By
#from src.system_under_test.ui.github_ui import BaseApp
class LoginPage():

    URL = "https://github.com/login"

    # IDs of page elements
    LOGIN_FLD = (By.ID,"login_field")
    PASSWORD_FLD = (By.ID, "password")
    SING_IN_BUTTON = (By.NAME, "commit")

    def __init__(self, app) -> None:
        self.app = app
        #super().__init__()
        # user methods

    def try_login(self, username: str, password: str):
        self.app.enter_text(locator=self.LOGIN_FLD, text=username)
        self.app.enter_text(locator=self.PASSWORD_FLD, text=password)


    def navigate_to(self):
        self.app.navigate_to(self.URL)

        # check functions

    def check_wrong_creds_message(self, message):
        # find error message
        # check if message is equal to "BLA" text
        return self.app.find_text(text=message)

    def check_documentation_link(self):
        pass

