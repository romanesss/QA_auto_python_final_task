import time
from selenium.common.exceptions import NoSuchElementException
from .base_page import  BasePage
from selenium.webdriver.common.by import By
import selenium

class MainPage(BasePage):

    def go_to_login_page(self):
        #time.sleep(10)
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert  self.is_element_present(By.CSS_SELECTOR,"#login_link_invalid"),\
            "Login link is not present"

    def is_element_present(self, how ,what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException :
            return False
        return True