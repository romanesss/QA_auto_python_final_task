from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException
class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        # берем ссылку из url
        find_link = self.browser.current_url
        assert link in find_link , "'login' not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "*** No login form!!! ***"

        #проверки полей формы логина
        #assert self.is_element_present(*LoginPageLocators.LOGIN_LOGIN),     "*** No login form element login    !!! ***"
        #assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD),  "*** No login form element password !!! ***"


    def should_be_register_form(self):

        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM) , "*** No registration form!!! ***"

        #Проверки полей формы регистрации
        #assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTRATION) ,    "*** No registration form element login            !!! ***"
        #assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION) , "*** No registration form elements password        !!! ***"
        #assert self.is_element_present(*LoginPageLocators.CONFIRM_PASSWORD),       "*** No registration form elements confirm pasword !!! ***"