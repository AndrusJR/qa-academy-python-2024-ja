from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class BaseApp:

    def __init__(self, browser) -> None:
        self.browser = browser

    def open_browser(self):
        self.browser.open()

    def navigate_to(self, url):
        self.browser.get(url)

    def wait_and_click(self, locator, timeout=15):
        # read what is implicit and explicit waiters
        elem = self.browser.find_element(locator)
        elem.click()

        return True

    def find_text(self, text):
        if self.browser.find_element(By.XPATH ,f"//*[contains(text(), '{text}')]"):

            return True

        raise RuntimeError(f"expected text '{text}' is not present")


    def enter_text(self, locator, text):
        elem = self.browser.find_element(*locator)
        elem.clear()
        elem.send_keys(text)
        time.sleep(2)
        if elem.get_attribute('value') != text:
            raise RuntimeError(f"Text {text} is not entered to {locator} element")


        elem.send_keys(Keys.RETURN)

        return True

    def close_browser(self):
        self.browser.close()       
