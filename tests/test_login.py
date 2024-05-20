import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.system_under_test.ui.github_ui import GitHubUI
from conftest import *
def test_negative_login_updated(tested_instance = GitHubUI(browser=driver)):
    """Summary: Test negative login attemp
    Steps:
    1. Navigate to login page
    2. Enter wrong creds
    3. Click login/signin button

    Expected result
    Error saying BLA appeared
    """
    # 1. Navigate to login page
    tested_instance.login_page.navigate_to()

    # 2. Enter wrong creds
    tested_instance.try_login(username="ksdnkjfnd", password="ksdnkjfnd")

    # Expected result
    assert tested_instance.check_wrong_creds_message(message="Incorrect username or password.")

    # CleanUP
    tested_instance.close()  # webdriver method - BAD

