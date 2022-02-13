import time
#from selenium.common.exceptions import  import имя_исключения
from .base_page import  BasePage
from selenium.webdriver.common.by import By
import selenium

class MainPage(BasePage):

    def go_to_login_page(self):
        #time.sleep(10)
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR,"#login_link_invalid")

    """def is_element_present(self, how ,what):
        try:
            self.browser.find_element(how, what)
        except (имя_исключения) :
            return False
        return True"""